#!/bin/bash
#ip=$(hostname -I | awk '{print $1}')
ip=$(ifconfig | grep 'inet ' | awk '{print $2}' | tail -n 1)
if [ "$ip" = "127.0.0.1" ]; then
  ip=$(hostname -I | awk '{print $1}')
fi
sub="${ip%${ip##*.}}"
# net="*"
net="0/24"
subnet="$sub$net"
nmap -sn $subnet | awk '/^Nmap scan/{print $5}'