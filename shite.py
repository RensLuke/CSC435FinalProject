import zlib
from screenshot import ScreenShotObj
import pygame

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
WIDTH = 1920
HEIGHT = 1080
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

            pixels = zlib.decompress(chunk)

            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
            # Display the picture
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)

            pygame.event.get()
            successCounter += 1
            co += 1
            print('co = ', co)

    finally:
        print('Successes = ' + str(successCounter))
        break


