#!/bin/bash

# Get the MAC address of the first Ethernet interface (en0)
ethernet_mac=$(ifconfig en0 | grep 'ether' | awk '{print $2}')

# Print the MAC address
echo $ethernet_mac