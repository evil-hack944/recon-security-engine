import socket
import json
import requests
from concurrent.futures import ThreadPoolExecutor

def get_service_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        s.connect((ip, port))
        if port in [80, 443, 8080]:
            s.sendall(b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n")
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        return banner.splitlines()[0] if banner else "No Banner Detected"
    except Exception:
        return "Banner Grab Failed"

def check_subdomain(target, sub):
    subdomain = f"{sub}.{target}"
    url = f"http://{subdomain}"
    try:
        response = requests.get(url, timeout=2)
        return {"subdomain": subdomain, "status_code": response.status_code}
    except requests.RequestException:
        return None

def run_subdomain_scan(domain):
    print("\n[*] Starting Subdomain Enumeration Engine...")
    common_subdomains = [
        "admin", "api", "mail", "dev", "test", "staging", 
        "portal", "blog", "vpn", "shop", "app", "dashboard"
    ]
    
    discovered = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_subdomain, domain, sub) for sub in common_subdomains]
        for future in futures:
            res = future.result()
            if res:
                print(f"    [+] Active Subdomain: {res['subdomain']} [Status: {res['status_code']}]")
                discovered.append(res)
                
    return discovered

def run_recon(domain):
    print(f"\n[*] Recon Engine Active Target: {domain}")
    print("=" * 50)
    
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"[+] Base IP Resolved: {ip_address}")
        
        common_ports = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 8080: "HTTP-ALT"}
        discovered_services = []
        
        print("\n[*] Auditing Open Services & Banners...")
        for port, service_name in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            if sock.connect_ex((ip_address, port)) == 0:
                sock.close()
                banner = get_service_banner(ip_address, port)
                print(f"    [+] Port {port} ({service_name}) OPEN | Banner: {banner}")
                discovered_services.append({"port": port, "service": service_name, "banner": banner})
            else:
                sock.close()
                
        subdomains = run_subdomain_scan(domain)
        
        return {
            "target": domain,
            "ip": ip_address,
            "services": discovered_services,
            "subdomains": subdomains
        }
        
    except socket.gaierror:
        print(f"[-] Error: Could not resolve hostname {domain}")
        return None

if __name__ == "__main__":
    target = input("Enter Target Domain: ").strip()
    if target:
        results = run_recon(target)
        if results:
            with open(f"audit_{target.replace('.', '_')}.json", "w") as f:
                json.dump(results, f, indent=4)
            print(f"\n[+] Scan Audit Log saved as 'audit_{target.replace('.', '_')}.json'")