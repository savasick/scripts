#!/bin/bash
#adapter=$(find /sys/class/net ! -type d | xargs --max-args=1 realpath | awk -F\/ '/pci/{print $NF}')
#IP=$(ifconfig $adapter | grep 'inet ' | awk '{print $2}')
ip=$(ifconfig | grep 'inet ' | awk '{print $2}' | tail -n 1)
if [ "$ip" = "127.0.0.1" ]; then
  ip=$(hostname -I | awk '{print $1}')
fi
echo "Scanning open ports on $ip"
nmap -p- $ip | grep "open"