import socket
import math
from screenshot import ScreenShotObj

UDP_IP_ADDRESS = '239.1.1.1'
UDP_PORT_NO = 6789
segment_size = 64000
sent = 0

while True:
    SS = ScreenShotObj()
    chunk = SS.takescreenshot()
    # print(len(chunk))
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    clientSock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton('192.168.86.36'))
    clientSock.sendto((str(math.ceil((len(chunk) / segment_size))).encode('utf-8')), (UDP_IP_ADDRESS, UDP_PORT_NO))
    # print(math.ceil((len(chunk) / 64000)))
    holder = segment_size
    holder2 = segment_size + segment_size
    sent += 1
    for i in range(int(math.ceil((len(chunk)/segment_size)))):
        if i == 0:
            clientSock.sendto(chunk[:holder], (UDP_IP_ADDRESS, UDP_PORT_NO))
        elif i == int(math.ceil((len(chunk)/segment_size))) - 1:
            clientSock.sendto(chunk[holder:], (UDP_IP_ADDRESS, UDP_PORT_NO))
            break
        else:
            clientSock.sendto(chunk[holder:holder2], (UDP_IP_ADDRESS, UDP_PORT_NO))
            holder = holder2
            holder2 = holder2 + segment_size

    # clientSock.sendto(b'fin'), (UDP_IP_ADDRESS, UDP_PORT_NO)
    print(sent)
