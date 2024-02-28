# Detect arpspoof

### install

```bash
sudo apt-get install python3-pip
pip3 install --pre scapy[basic]
```

or

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
#

### start
```bash
sudo python3 arpDetector.py
```

# ARP spoof

start
```bash
sudo python3 arpSpoof.py <victim_ip> <router_ip>
# like so
sudo python3 arpSpoof.py 192.168.1.100 192.168.1.1
```


to know about netusers
```bash
sudo netdiscover
```