import scapy
import scapy.layers
import scapy.layers.inet
import scapy.sendrecv

# Implement your ICMP sender here

receiver_ip = "172.18.0.3"
ip_packet = scapy.layers.inet.IP(dst=receiver_ip, ttl=1)

icmp_request = scapy.layers.inet.ICMP()
packet = ip_packet / icmp_request

scapy.sendrecv.send(packet)
