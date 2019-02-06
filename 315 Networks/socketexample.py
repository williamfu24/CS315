import socket
hostname = 'www.twitter.com'
addr = socket.gethostbyname(hostname)
print('The address of', hostname, 'is', addr)
