import nmap

def scan_ports(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, '1-1024')
    open_ports = [port for port in scanner[ip]['tcp'] if scanner[ip]['tcp'][port]['state'] == 'open']
    return open_ports
