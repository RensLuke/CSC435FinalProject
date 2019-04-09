from zlib import decompress
import socket
from screenshot import ScreenShotObj
import pygame

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
WIDTH = 1920
HEIGHT = 1080

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

data, addr = serverSock.recvfrom(32)
i = 0
chunk = b''
num = data.decode('utf-8')
print(num)
while True:
    print(i)
    i += 1
    data1, addr1 = serverSock.recvfrom(64000)
    chunk = chunk + data1
    if i == int(num):
        break

with open('test.txt', 'rb') as filereader:
    display = filereader.read()
if display == chunk:
    print('They are the same')

pygame.init()
pygame.display.set_caption('Rolt VNC')
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
watching = True


while watching:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            watching = False
            break

    pixels = decompress(display)
    # Create the Surface from raw pixels
    img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')

    # Display the picture
    screen.blit(img, (0, 0))
    pygame.display.flip()
    clock.tick(60)




