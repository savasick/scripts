#!/bin/bash

adapter=$(find /sys/class/net ! -type d | xargs --max-args=1 realpath | awk -F\/ '/pci/{print $NF}')

cat /sys/class/net/$adapter/address

