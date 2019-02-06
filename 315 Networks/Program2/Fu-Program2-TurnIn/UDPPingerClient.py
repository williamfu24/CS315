#William Fu
#UDPPingerClient.py
#i was getting an error (TypeError: a bytes-like object is required, not 'str')
#and when research I was told to put .encode() which results in a b to be printed


import time
from socket import *

#send ping 10 times
for ping in range(10):
    #UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    #1 second timeout
    clientSocket.settimeout(1.0)
    #message and location
    message = 'test'.encode()
    address = ("127.0.0.1", 4444)
    #Send ping
    start = time.time()
    clientSocket.sendto(message, address)
    #echo back
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print(f'{ping+1} {data} {elapsed}')
    #packet lost
    except timeout:
        print (ping+1)
        print ('    Request Timed Out')
