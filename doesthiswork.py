from zlib import decompress
import socket
from screenshot import ScreenShotObj


UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
WIDTH = 1920
HEIGHT = 1080

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    try:
        data, addr = serverSock.recvfrom(32)
    except OSError:
        print('bad receive')
    else:
        chunk = b''
        num = data.decode('utf-8')

        for j in range(int(num)):
            data, addr = serverSock.recvfrom(64000)
            chunk = chunk + data

        with open('test.txt', 'rb') as binary_file:
            OGchunk = binary_file.read()

        if chunk == OGchunk:
            print("They are the same")
        else:
            print("They are not the same")

    '''
    pygame.init()
    pygame.display.set_caption('Rolt VNC')
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    watching = True
    
    while watching:
        print("here")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                watching = False
                break
    
        pixels = decompress(chunk)
        # Create the Surface from raw pixels
        img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
    
        # Display the picture
        screen.blit(img, (0, 0))
        pygame.display.flip()
        clock.tick(60)
    '''



