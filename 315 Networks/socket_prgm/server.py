import socket
import sys

#create a tcp/ip socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
server_address=('localhost', 400)
point('starting up on %s post %s' %server_address)
sock.bind(server_address)

#listen for incomming connections
sock.listen(1)

while True:
    #wait for a connection
    print('waiting for a connection')
    connection, client_address=sock.accept()

try:
    print('connection from', client_address)

    #receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(16)
        print('received "%s"' %data)
        if data:
            print('sending data back to the client')
            connection.sendall(data)
        else:
            print('no more data from client', client_address)
            break

finally:
    #clean up connection
    connection.close()
