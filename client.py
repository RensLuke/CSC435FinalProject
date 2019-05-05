import zlib
import socket
import struct
from screenshot import ScreenShotObj
import pygame
import threading


def get_sfa_ip():
    ipList = socket.gethostbyname_ex(socket.gethostname())[2]
    for x in range(len(ipList)):
        if '144.96' in ipList[x]:
            return ipList[x]


UDP_IP_ADDRESS = '239.1.1.1'
UDP_PORT_NO = 6789
server_address = ('', UDP_PORT_NO)
WIDTH = 1920
HEIGHT = 1080
OSErrorCount = 0
CompressionErrorCount = 0
pygameErrorCount = 0
successCounter = 0

my_ip = get_sfa_ip()
# my_ip = '192.168.0.14'  # For testing

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(server_address)
group = socket.inet_aton(UDP_IP_ADDRESS)
mreq = struct.pack('4s4s', group, socket.inet_aton(my_ip))
serverSock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
print("Starting on IP:", my_ip)
pygame.init()
pygame.display.set_caption('Rolt VNC')
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
watching = True

while True:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
            else:
                try:
                    data, addr = serverSock.recvfrom(32)
                    num = data.decode('utf-8')
                    print(num)
                except OSError:
                    print('Bad Receive')
                    OSErrorCount += 1
                else:
                    chunk = b''
                    for j in range(int(num)):
                        data, addr = serverSock.recvfrom(64000)
                        chunk = chunk + data
                    try:
                        zobj = zlib.decompressobj()
                        pixels = zobj.decompress(chunk)
                    except zlib.error:
                        print("Compression Error")
                        CompressionErrorCount += 1
                    else:
                        # Create the Surface from raw pixels
                        try:
                            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
                        except ValueError:
                            print("pygame error")
                            pygameErrorCount += 1
                        else:
                            # Display the picture
                            screen.blit(img, (0, 0))
                            pygame.display.flip()
                            clock.tick(60)
                            successCounter += 1
                            print("Success!")
        break
print("bad receive = ", OSErrorCount)
print("compression errors = ", CompressionErrorCount)
print("pygame errors = ", pygameErrorCount)
print("successes = ", successCounter)
