import socket
import json
from datetime import datetime

def get_service_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.connect((ip, port))
        if port in [80, 443, 8080]:
            s.sendall(b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n")
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        return banner if banner else "No Banner Detected"
    except Exception:
        return "Banner Grab Failed"

def run_recon(domain):
    print(f"\n[*] Recon Engine Active Target: {domain}")
    print("=" * 50)
    
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"[+] IP Resolved: {ip_address}")
        
        common_ports = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 8080: "HTTP-ALT"}
        discovered_services = []
        
        for port, service_name in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            
            if sock.connect_ex((ip_address, port)) == 0:
                sock.close()
                banner = get_service_banner(ip_address, port)
                discovered_services.append({
                    "port": port,
                    "service": service_name,
                    "banner": banner
                })
            else:
                sock.close()
                
        scan_data = {
            "target": domain,
            "ip": ip_address,
            "scan_time": str(datetime.now()),
            "services": discovered_services
        }
        
        # --- AUDIT SUMMARY LOGGING ---
        log_filename = f"audit_{domain.replace('.', '_')}.txt"
        with open(log_filename, "w") as f:
            f.write(f"=== RECON AUDIT SUMMARY FOR {domain} ===\n")
            f.write(f"Timestamp: {scan_data['scan_time']}\n")
            f.write(f"Target IP: {ip_address}\n")
            f.write("-" * 40 + "\n")
            for item in discovered_services:
                f.write(f"Port {item['port']} ({item['service']}): OPEN\n")
                f.write(f"Banner: {item['banner']}\n\n")
        
        print(f"\n[+] Audit Summary saved automatically to: {log_filename}")
        return scan_data

    except socket.gaierror:
        print(f"[-] Error: Could not resolve hostname {domain}")
        return None

if __name__ == "__main__":
    target = input("Enter Target Domain: ").strip()
    if target:
        results = run_recon(target)
        if results:
            print("\n[+] Raw Audit JSON:")
            print(json.dumps(results, indent=4))