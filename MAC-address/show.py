#!/usr/bin/env python3
from os import listdir
from os.path import islink, realpath, join

interfaces = [i for i in listdir("/sys/class/net") if islink(join("/sys/class/net", i))]
interfaces = [i for i in interfaces if not realpath(join("/sys/class/net", i)).startswith(("/sys/devices/virtual", "/sys/devices/vif"))]

print(interfaces[0])