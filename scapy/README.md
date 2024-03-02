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

### start to detect xmas scan
```bash
sudo python3 xmasDetect.py
```


### start Syn scan
```bash
sudo python synScan.py 192.168.1.1 80 443
```

