#!/bin/bash

echo "Enter your IP"

read IP

echo "Enter your Port"

read port

printf "Select a Scan \n 1 for Aggresive \n 2 for Syn \n 3 for TCP \n"

read st

if [ $st -eq 1 ]
then
    nmap -A $IP -p $port

elif [ $st -eq 2 ]
then
    nmap -sS -O -sV $IP -p $port

elif [ $st -eq 3 ]
then
    nmap -sT -O -sV $IP -p $port
fi

