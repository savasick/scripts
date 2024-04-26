#!/bin/bash
#ip=$(hostname -I | awk '{print $1}')
ip=$(ifconfig | grep 'inet ' | awk '{print $2}' | tail -n 1)
sub="${ip%${ip##*.}}"
# net="*"
net="0/24"
subnet="$sub$net"
nmap -sn $subnet | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " "substr($0, index($0,$3)) }'