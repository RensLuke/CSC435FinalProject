import zlib
import socket
import struct
import helper
import pygame

# Set defaults
network = helper.NetworkingObj()
ip_addr = network.get_sfa_ip()
multicast_addr = '239.1.1.1'
resolution = '1920 x 1080'


def run_me(pIP, pMulti, pRes, pSaved):
    global ip_addr, multicast_addr, resolution
    if pSaved:
        ip_addr = pIP
        multicast_addr = pMulti
        resolution = pRes
    start()


def start():
    global ip_addr, multicast_addr, resolution
    UDP_IP_ADDRESS = multicast_addr
    UDP_PORT_NO = 6789
    server_address = ('', UDP_PORT_NO)
    resolution = resolution.split()
    width = int(resolution[0])
    height = int(resolution[2])
    OSErrorCount = 0
    CompressionErrorCount = 0
    pygameErrorCount = 0
    successCounter = 0

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind(server_address)
    serverSock.settimeout(5)
    mreq = struct.pack('4s4s', socket.inet_aton(UDP_IP_ADDRESS), socket.inet_aton(ip_addr))
    serverSock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    print("Starting on IP:", ip_addr)
    print("Multicast:", multicast_addr)
    print(width, height)

    # Set up Pygame stuff
    pygame.init()
    pygame.display.set_caption('Jack Cast')
    icon = pygame.image.load('GUI/Icons/jack_cast_icon.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    watching = True
    width2 = width
    height2 = height

    while True:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    pygame.quit()
                    break
                elif event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                    width2 = event.dict['size'][0]
                    height2 = event.dict['size'][1]
            else:
                try:
                    data, addr = serverSock.recvfrom(32)
                    num = data.decode('utf-8')
                except socket.timeout:
                    pygame.quit()
                    break
                except OSError:
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
                        CompressionErrorCount += 1
                    else:
                        # Create the Surface from raw pixels
                        try:
                            img = pygame.image.fromstring(pixels, (width, height), 'RGB')
                        except ValueError:
                            pygameErrorCount += 1
                        else:
                            # Display the picture
                            screen.blit(pygame.transform.smoothscale(img, (width2, height2)), (0, 0))
                            pygame.display.flip()
                            clock.tick(60)
                            successCounter += 1
        break


