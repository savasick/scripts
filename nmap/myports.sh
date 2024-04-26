#!/bin/bash
#adapter=$(find /sys/class/net ! -type d | xargs --max-args=1 realpath | awk -F\/ '/pci/{print $NF}')
#IP=$(ifconfig $adapter | grep 'inet ' | awk '{print $2}')
ip=$(ifconfig | grep 'inet ' | awk '{print $2}' | tail -n 1)
echo "Scanning open ports on $IP"
nmap -sT -O -p- $IP | grep "open"