# MAC Address

### at Linux

#### show mac with bash
```bash
bash show.sh
```
at macos
```bash
bash mac_show.sh
```


#### or

```bash
adapter=$(find /sys/class/net ! -type d | xargs --max-args=1 realpath | awk -F\/ '/pci/{print $NF}')

cat /sys/class/net/$adapter/address
```
#

### generate random mac address

```bash
bash generate.sh
```

#

### changes mac address

#### bash/shell

```bash
bash random.sh
```

or

```bash
adapter=$(find /sys/class/net ! -type d | xargs --max-args=1 realpath | awk -F\/ '/pci/{print $NF}')

ifconfig $adapter down 
macchanger -r $adapter
ifconfig $adapter up
```

#


### change mac by python
```bash
python3 main.py
```

#

### at macOS


```bash
bash mac_random.sh
```