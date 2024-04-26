#!/bin/bash
# sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -z

generated_mac=$(openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//')

sudo ifconfig en0 ether $generated_mac
ifconfig en0 | grep ether