import psutil, random, subprocess, netifaces

R ="\033[1;31m";
Y ="\033[1;33m";
C ="\033[1;36m";
W ="\033[0m";


def show_mac(adapter):
    mac = netifaces.ifaddresses(adapter)[netifaces.AF_LINK]
    mac = mac[0]['addr']
    print(Y , mac, R)

def get_mac(adapter):
    mac = netifaces.ifaddresses(adapter)[netifaces.AF_LINK]
    mac = mac[0]['addr']
    return mac

def get_adapters():
    addresses = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    adapters = {}
    i=0

    for intface, addr_list in addresses.items():
        if any(getattr(addr, 'address').startswith("169.254") for addr in addr_list):
            continue
        elif intface in stats and getattr(stats[intface], "isup"):
            adapters[i] = intface
            i += 1
    
    return adapters

def get_choosen_adapters(adapters):
    string=""

    for num in adapters:
        string += "%d) %s \n" % (num, adapters[num])
    print(C)
    resp = None
    
    while(resp not in adapters.keys()):
        print(R, "Enter a valid option", C)
        resp = int(input("\nPlease enter number of NET adapter (abort CTRL+C)\n"+string))
        resp == None
    print(R ,"net Adapter =", C,adapters[resp])
    adapter = adapters[resp]
    return str(adapter)

def random_mac():
    random_mac = [0x00, 0x50, 0x56, random.randint(0x00,0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    mac_addr = ":".join(map(lambda x: "%02x" %x,random_mac))
    return mac_addr

def mac_spoof(mac_addr, adapter):
    print(R,"Old MAC address")
    show_mac(adapter)
#    subprocess.call(["ip", "link",  "show", adapter])
#    subprocess.call(["ifdown", adapter])
    subprocess.call(["ip", "link",  "set", adapter, "down"])
    subprocess.call(["ip", "link",  "set", adapter, "addr", mac_addr])
    subprocess.call(["ip", "link",  "set", adapter, "up"])
    print(C, "New MAC address")
    show_mac(adapter)
#    subprocess.call(["ip", "link",  "show", adapter])

if __name__ == "__main__":
    adapter = get_choosen_adapters(get_adapters())
    mac_addr = random_mac()
    mac_spoof(mac_addr, adapter)
    mac = get_mac(adapter)

