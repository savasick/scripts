from scapy.all import IP, ICMP, TCP, sr1, send
import argparse

def icmp_probe(ip):
    icmp_packet = IP(dst=ip) / ICMP()
    response = sr1(icmp_packet, timeout=10)
    return response != None

def syn_scan(ip, ports):
    for port in ports:
        syn_packet = IP(dst=ip) / TCP(sport=32768, dport=port, flags="S")

        response = sr1(syn_packet, timeout=3, verbose=0)

        if response is not None:
            if 'SYN/ACK' in str(response.flags):
                rst_packet = IP(dst=ip) / TCP(sport=response.sport, dport=port, flags="R")
                send(rst_packet, verbose=0)
                print(f"Port {port} is open")
            elif 'RST' in str(response.flags):
                print(f"Port {port} is closed")
            elif 'RST/ACK' in str(response.flags):
                print(f"Port {port} is closed")
        else:
            print(f"No response from {ip}:{port}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("ports", nargs="+", type=int, help="Ports to scan")
    args = parser.parse_args()

    if icmp_probe(args.ip):
        syn_scan(args.ip, args.ports)
    else:
        print("ICMP Probe Failed")