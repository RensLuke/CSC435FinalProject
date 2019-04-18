import zlib
import socket
from screenshot import ScreenShotObj
import pygame
import threading

UDP_IP_ADDRESS = "0.0.0.0"
UDP_PORT_NO = 6789
WIDTH = 1920
HEIGHT = 1080
buffer = []
OSErrorCount = 0
CompressionErrorCount = 0
pygameErrorCount = 0
successCounter = 0


serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print("Starting")
pygame.init()
pygame.display.set_caption('Rolt VNC')
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
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
                        print(len(pixels))
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
