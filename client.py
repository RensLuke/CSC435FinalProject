import zlib
import socket
import struct
from screenshot import ScreenShotObj
import pygame
import threading

UDP_IP_ADDRESS = '239.1.1.1'
UDP_PORT_NO = 6789
server_address = ('', UDP_PORT_NO)
WIDTH = 1980
HEIGHT = 1080
buffer = []
OSErrorCount = 0
CompressionErrorCount = 0
pygameErrorCount = 0
successCounter = 0


serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(server_address)
group = socket.inet_aton(UDP_IP_ADDRESS)
mreq = struct.pack('4s4s', group, socket.inet_aton('192.168.86.35'))
serverSock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
print("Starting")
pygame.init()
pygame.display.set_caption('Rolt VNC')
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()
watching = True

co = 0
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
                            img = pygame.transform.scale(img, (1280, 720))
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
