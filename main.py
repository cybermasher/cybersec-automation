from modules.port_scanner import scan_ports
from modules.vulnerability_scanner import check_vulnerabilities
from modules.network_monitor import monitor_traffic

def main():
    print("Starting Cybersec Automation...")
    
    # Scan for open ports
    target_ip = "192.168.1.1"
    open_ports = scan_ports(target_ip)
    print(f"Open Ports on {target_ip}: {open_ports}")
    
    # Check for vulnerabilities
    vulnerabilities = check_vulnerabilities(target_ip)
    print(f"Vulnerabilities on {target_ip}: {vulnerabilities}")
    
    # Monitor network traffic
    monitor_traffic()

if __name__ == "__main__":
    main()
