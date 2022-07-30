import socket
import os
import sys

host = str(input("Enter irc server ip: "))
port = 5835
chunksize=512
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
try:
    s.connect((host, port))
except ConnectionRefusedError:
    print("[-] Server is offline.")
    exit(0)
print("[+] Connected.")

def send():
    msg = str(input('Send your message to the people: '))
    if len(msg) <= 512:
        s.send(str.encode(msg))
    
while True:
    send()

