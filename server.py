import socket
import math
import helper

# Set defaults
network = helper.NetworkingObj()
ip_addr = network.get_sfa_ip()
multicast_addr = '239.1.1.1'
resolution = '1600 x 900'


def run_me(pIP, pMulti, pRes, pSaved):
    global ip_addr, multicast_addr, resolution
    if pSaved:
        ip_addr = pIP
        multicast_addr = pMulti
        resolution = pRes
    start()


def start():
    # Defining variables
    global ip_addr, multicast_addr, resolution

    UDP_IP_ADDRESS = multicast_addr
    UDP_PORT_NO = 6789
    segment_size = 64000
    sent = 0
    resolution = resolution.split()
    width = int(resolution[0])
    height = int(resolution[2])

    while True:
        # Declaring screenshot object
        SS = helper.ScreenShotObj()
        chunk = SS.takescreenshot(width, height)

        # Setting up socket
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # Declaring UDP socket
        serverSock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(ip_addr))  # Telling kernel to send packets as multicast
        serverSock.sendto((str(math.ceil((len(chunk) / segment_size))).encode('utf-8')), (UDP_IP_ADDRESS, UDP_PORT_NO))  #  finding/sending how many chunks to send
        
        # declaring holder objects for chunking
        holder = segment_size
        holder2 = segment_size + segment_size
        sent += 1
        for i in range(int(math.ceil((len(chunk)/segment_size)))):  # iterating i many chunks
            if i == 0:
                serverSock.sendto(chunk[:holder], (UDP_IP_ADDRESS, UDP_PORT_NO))  # sending first chunk
            elif i == int(math.ceil((len(chunk)/segment_size))) - 1:  # sending last chunk
                serverSock.sendto(chunk[holder:], (UDP_IP_ADDRESS, UDP_PORT_NO))
                break
            else:
                serverSock.sendto(chunk[holder:holder2], (UDP_IP_ADDRESS, UDP_PORT_NO)) # sending all the chunks inbetween
                holder = holder2
                holder2 = holder2 + segment_size

        print(sent)
