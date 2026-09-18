import socket
import sys

def get_target_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Target Domain: {domain}")
        print(f"[+] IP Address: {ip}")
        return ip
    except socket.gaierror:
        print("[-] Error: Could not resolve domain.")
        sys.exit()

def scan_ports(ip, ports):
    print("\n[*] Starting Basic Port Scan...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"    [OPEN] Port {port}")
        else:
            print(f"    [CLOSED/FILTERED] Port {port}")
        s.close()

if __name__ == "__main__":
    print("=" * 45)
    print("      RECON SECURITY ENGINE v1.0")
    print("=" * 45)
    
    target = input("Enter target domain (e.g., scanme.nmap.org): ").strip()
    target_ip = get_target_ip(target)
    
    # Common ports to scan
    common_ports = [21, 22, 80, 443, 8080]
    scan_ports(target_ip, common_ports)
