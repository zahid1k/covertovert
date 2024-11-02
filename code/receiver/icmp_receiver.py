import scapy
import scapy.layers
import scapy.layers.inet
import scapy.sendrecv

# Implement your ICMP receiver here


def handle_packet(packet):
    if scapy.layers.inet.IP in packet and scapy.layers.inet.ICMP in packet and packet[scapy.layers.inet.IP].ttl == 1:
        packet.show()

scapy.sendrecv.sniff(filter="icmp", prn=handle_packet, count=1)