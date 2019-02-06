#code for client side of the program
import socket
import sys

#create a tcp/ip socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the socket to the port where the server is listening
server_address=('localhost', 400)
print(sys.stderr, 'connection to %s port%s' %server_address)
sock.connect(server_address)

try:
    #send data
    message = 'This is the message. It will be repeated.'
    print(sys.stderr, 'sending "%s"' %message)
    sock.sendall(message.encode())

    #look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received<amount_expected:
        data=sock.recv(16)
        amount_received+=len(data)
        print(sys.stderr, 'received "%s"' %data)

finally:
    print(sys.stderr, 'closing socket;)
          sock.close()
