import zlib
import socket
from screenshot import ScreenShotObj
import pygame

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
WIDTH = 1920
HEIGHT = 1080

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

pygame.init()
pygame.display.set_caption('Rolt VNC')
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
watching = True
decompressCounter = 0
badreceiveCounter = 0
successCounter = 0

while True:
    try:
        while watching:
            a = 'err '
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
            try:
                data, addr = serverSock.recvfrom(32)
            except OSError:
                badreceiveCounter += 1
                # print('bad receive')
                a += 'badRec '
            else:
                chunk = b''
                num = data.decode('utf-8')

                for j in range(int(num)):
                    data, addr = serverSock.recvfrom(64000)
                    chunk = chunk + data
                try:
                    pixels = zlib.decompress(chunk)
                    # Create the Surface from raw pixels
                    img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
                    # Display the picture
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    clock.tick(60)
                    successCounter += 1
                    print("Success!")
                except zlib.error:
                    decompressCounter += 1
                    # print("decompress error")
                    a += 'decomp '
            if a != 'err ':
                print(a)
    finally:
        serverSock.close()
        print('Decompress Error = ' + str(decompressCounter))
        print('Bad Receive Error = ' + str(badreceiveCounter))
        print('Successes = ' + str(successCounter))
        break


