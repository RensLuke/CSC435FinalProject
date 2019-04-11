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

            SS = ScreenShotObj()
            chunk = SS.takescreenshot()
            # buff = threading.Thread(target=packet_buffer())
            # buff.start()

            pixels = zlib.decompress(chunk)
            # pixels = chunk
            # pixels = zlib.decompress(buffer[co])
            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
            # Display the picture
            screen.blit(img, (0, 0))
            pygame.display.flip()
            # clock.tick(60)
            successCounter += 1
            co += 1
            print('co = ', co)

    finally:
        print('Decompress Error = ' + str(decompressCounter))
        print('Bad Receive Error = ' + str(badreceiveCounter))
        print('Successes = ' + str(successCounter))
        break


