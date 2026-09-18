import socket
import json

def get_target_info(domain):
    """
    Resolves domain to IP and performs basic network checks
    """
    print(f"\n[*] Initiating Recon Engine for: {domain}")
    print("=" * 45)
    
    try:
        # Resolve IP Address
        ip_address = socket.gethostbyname(domain)
        print(f"[+] IP Address Resolved: {ip_address}")
        
        # Target Ports to scan
        common_ports = {
            21: "FTP",
            22: "SSH",
            80: "HTTP",
            443: "HTTPS",
            8080: "HTTP-ALT"
        }
        
        open_ports = []
        print("\n[*] Scanning Common Infrastructure Ports...")
        
        for port, service in common_ports.items():
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0) # 1 second timeout
            
            result = s.connect_ex((ip_address, port))
            if result == 0:
                print(f"    [OPEN] Port {port} ({service})")
                open_ports.append({"port": port, "service": service, "status": "OPEN"})
            else:
                print(f"    [CLOSED] Port {port} ({service})")
            s.close()
            
        return {
            "target": domain,
            "ip": ip_address,
            "open_ports": open_ports
        }
        
    except socket.gaierror:
        print(f"[-] Error: Could not resolve hostname {domain}")
        return None

if __name__ == "__main__":
    target_domain = input("Enter Target Domain (e.g., scanme.nmap.org): ").strip()
    if target_domain:
        results = get_target_info(target_domain)
        if results:
            print("\n[+] Recon Complete. Raw Output:")
            print(json.dumps(results, indent=4))