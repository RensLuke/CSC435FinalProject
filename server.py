import socket
import math
import helper

# ip_addr = '192.168.0.14'  # For testing
network = helper.NetworkingObj()
ip_addr = network.get_sfa_ip()
multicast_addr = '239.1.1.1'
resolution = '1920 x 1080'


def run_me(pIP, pMulti, pRes, pSaved):
    global ip_addr, multicast_addr, resolution
    if pSaved:
        ip_addr = pIP
        multicast_addr = pMulti
        resolution = pRes
    start()


def start():
    UDP_IP_ADDRESS = multicast_addr
    UDP_PORT_NO = 6789
    segment_size = 64000
    sent = 0

    while True:
        SS = helper.ScreenShotObj()
        chunk = SS.takescreenshot()
        # print(len(chunk))
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        clientSock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(ip_addr))
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
