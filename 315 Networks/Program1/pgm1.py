#import socket module
from socket import *
import socket
import sys

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr=('localhost', 444)
print('starting up on %s port %s' %server_addr)
serverSocket.bind(server_addr)
serverSocket.listen(1)
 
while True:
    print('Socket Running...')

    connectSocket, connect_Addr = serverSocket.accept()
    try:

        message = connectSocket.recv(1024)
        print (message, "::", message.split()[0], ":", message.split()[1])
        
        filename = message.split()[1]
        print(filename, '||', filename[1:])

        f = open(filename[1:])
        outputdata = f.read()

        print(outputdata)

        #connectSocket.send('\n')
        connectSocket.sendto("\HTTP/1.1 200 OK \n".encode('ascii'), connect_Addr)
        
        for i in range(0, len(outputdata)):
            connectSocket.sendto(outputdata[i].encode('ascii'), connect_Addr)
        connectSocket.sendto("\r\n".encode('ascii'), connect_Addr)
        #connectSocket.send(outputdata.encode('ascii'))
        connectSocket.close()
    except IOError:
        pass
        print('Returning 404')
        connectSocket.sendto("\HTTP/1.1 404 Not Found\r\n".encode('ascii'), connect_Addr)
        connectSocket.close()
    break

    connectSocket.close()
    serverSocket.close()

    sys.exit()
