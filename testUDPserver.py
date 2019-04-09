import socket
import pygame
from zlib import decompress

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

WIDTH = 1900
HEIGHT = 1000

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

'''
hold = b''
while True:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    watching = True

    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break
            data, addr = serverSock.recvfrom(32)
            i = 0
            num = data.decode('utf-8')
            print(num)
            if str(num) == '3' or str(num) == '4':
                while True:
                    i += 1
                    data1, addr1 = serverSock.recvfrom(64000)
                    hold = hold + data1
                    if i == 3 and num == '3':
                        break
                    elif i == 4 and num == '4':
                        break
            data = b''

            img = pygame.image.fromstring(hold, (WIDTH, HEIGHT), 'RGB')

            # Display the picture
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)
    except OSError:
        print("Sync Issue, try again")
'''

data, addr = serverSock.recvfrom(32)
i = 0
chunk = b''
num = data.decode('utf-8')
print(num)
while True:
    i += 1
    data1, addr1 = serverSock.recvfrom(64000)
    chunk = chunk + data1
    if i == int(num):
        break


with open('test.txt', 'rb') as filereader:
    display = filereader.read()

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


