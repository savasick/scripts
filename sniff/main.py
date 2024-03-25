from scapy.all import *

def process_packet(packet):
    if packet.haslayer(IP):
        print("Source IP: {}".format(packet[IP].src))
        print("Destination IP: {}".format(packet[IP].dst))
        if packet.haslayer(TCP):
            print("Source port: {}".format(packet[TCP].sport))
            print("Destination port: {}".format(packet[TCP].dport))

sniff(prn=process_packet, filter="tcp", store=0)