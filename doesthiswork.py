import zlib
import socket
from screenshot import ScreenShotObj
import pygame
import threading


UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
WIDTH = 1920
HEIGHT = 1080
buffer = []
buffer_counter = 0
decompressCounter = 0
badreceiveCounter = 0
successCounter = 0

'''
def packet_buffer():
    global buffer_counter
    p = 0
    while buffer_counter != 500:
        try:
            data, addr = serverSock.recvfrom(32)
            num = data.decode('utf-8')
        except OSError:
            print('bad receive')
        else:
            chunk = b''
            for j in range(int(num)):
                data, addr = serverSock.recvfrom(64000)
                chunk = chunk + data
            buffer.append(chunk)
            buffer_counter += 1
            print(buffer_counter)
            pygame.event.get()
'''

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
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
            
            else:
                try:
                    data, addr = serverSock.recvfrom(32)
                    num = data.decode('utf-8')
                except OSError:
                    print('bad receive')
                else:
                    chunk = b''
                    for j in range(int(num)):
                        data, addr = serverSock.recvfrom(64000)
                        chunk = chunk + data
                # buff = threading.Thread(target=packet_buffer())
                # buff.start()
                try:
                    pixels = zlib.decompress(chunk)
                    # Create the Surface from raw pixels
                    img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
                    # Display the picture
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    clock.tick(60)
                    successCounter += 1
                    co += 1
                    print('co = ', co)
                    if co == buffer_counter:
                        break
                    # print("Success!")
                except zlib.error:
                    decompressCounter += 1
                    print("decompress error")
    finally:
        serverSock.close()
        print('Decompress Error = ' + str(decompressCounter))
        print('Bad Receive Error = ' + str(badreceiveCounter))
        print('Successes = ' + str(successCounter))
        break


