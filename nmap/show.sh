#!/bin/bash
ip=$(hostname -I | awk '{print $1}')
sub="${ip%${ip##*.}}"
# net="*"
net="0/24"
subnet="$sub$net"
nmap -sn $subnet | awk '/^Nmap scan/{print $5}'