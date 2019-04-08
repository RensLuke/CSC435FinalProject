import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = 'hello test'
with open('test.jpg', 'rb') as binary_file:
    chunk = binary_file.read()

with open('test.txt', 'rb') as binary_file:
    chunk2 = binary_file.read()


print(len(chunk2))

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSock.sendto(chunk2, (UDP_IP_ADDRESS, UDP_PORT_NO))

