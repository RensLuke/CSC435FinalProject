import socket
import math
from screenshot import ScreenShotObj

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = 'hello test'


SS = ScreenShotObj()
chunk = SS.takescreenshot()
with open('test.txt', 'wb') as binary_file:
    binary_file.write(chunk)
print(len(chunk))
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto((str(math.ceil((len(chunk) / 64000))).encode('utf-8')), (UDP_IP_ADDRESS, UDP_PORT_NO))
print(math.ceil((len(chunk) / 64000)))
holder = 64000
holder2 = 0
if int(math.ceil((len(chunk)/64000))) == 3:
    for i in range(int(math.ceil((len(chunk)/64000)))):
        if i == 0:
            clientSock.sendto(chunk[:holder], (UDP_IP_ADDRESS, UDP_PORT_NO))
        elif i == 1:
            holder = holder + 64000
            clientSock.sendto(chunk[64000:holder], (UDP_IP_ADDRESS, UDP_PORT_NO))
        elif i == 2:
            clientSock.sendto(chunk[holder:], (UDP_IP_ADDRESS, UDP_PORT_NO))
elif int(math.ceil((len(chunk)/64000))) == 4:
    for i in range(int(math.ceil((len(chunk)/64000)))):
        if i == 0:
            clientSock.sendto(chunk[:holder], (UDP_IP_ADDRESS, UDP_PORT_NO))
        elif i == 1:
            holder = holder + 64000
            clientSock.sendto(chunk[64000:holder], (UDP_IP_ADDRESS, UDP_PORT_NO))
        elif i == 2:
            holder2 = holder + 64000
            clientSock.sendto(chunk[holder:holder2], (UDP_IP_ADDRESS, UDP_PORT_NO))
        elif i == 3:
            clientSock.sendto(chunk[holder2:], (UDP_IP_ADDRESS, UDP_PORT_NO))





