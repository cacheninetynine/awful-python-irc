# still only 1 way tho
import socket
import sys
s = socket.socket()
s.bind(("loaclhost",5835))
s.listen(10) # accept up to 10 users

while True:
    sc, address = s.accept()
    while (True):
        encmsg = sc.recv(512) # max msg length 512, you can make it higher
        decmsg = encmsg.decode()
        print("anon: "+decmsg)
