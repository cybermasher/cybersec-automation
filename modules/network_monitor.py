from scapy.all import sniff, IP

def monitor_traffic():
    def process_packet(packet):
        if packet.haslayer(IP):
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            print(f"Packet: {ip_src} -> {ip_dst}")

    sniff(prn=process_packet, filter="ip", count=10)
