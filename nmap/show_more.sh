#!/bin/bash
#ip=$(hostname -I | awk '{print $1}')
ip=$(ifconfig | grep 'inet ' | awk '{print $2}' | tail -n 1)
sub="$(echo "$ip" | cut -d. -f1-2).*."
# net=".*.*"
net="0/24"
subnet="$sub$net"
echo whats looking for $subnet
nmap -sn --min-rtt-timeout=100ms --max-retries=3 --host-timeout=60s $subnet | awk '/^Nmap scan/{print $5}'
