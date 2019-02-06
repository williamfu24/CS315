import socket
hostname = 'www.google.com'

addr = socket.gethostbyname(hostname)
info = socket.getaddrinfo(hostname, 80, proto=socket.IPPROTO_TCP)
machine = socket.gethostname()

print('The address of', hostname, 'is', addr)
print('The info for', hostname, 'is', info)
print('The Machine hosting the Python inerpreter is', machine, '.')
