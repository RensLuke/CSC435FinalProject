import zlib
import socket
import struct
import helper
import pygame


# ip_addr = '192.168.0.14'  # For testing
network = helper.NetworkingObj()
ip_addr = network.get_sfa_ip()
multicast_addr = '239.1.1.1'
resolution = '1920 x 1080'


def run_me(pIP, pMulti, pRes):
    global ip_addr, multicast_addr, resolution
    ip_addr = pIP
    multicast_addr = pMulti
    resolution = pRes
    start()


def start():
    UDP_IP_ADDRESS = multicast_addr
    UDP_PORT_NO = 6789
    server_address = ('', UDP_PORT_NO)
    WIDTH = 1920
    HEIGHT = 1080
    OSErrorCount = 0
    CompressionErrorCount = 0
    pygameErrorCount = 0
    successCounter = 0

    # my_ip = get_sfa_ip()
    # my_ip = '192.168.0.14'  # For testing

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind(server_address)
    group = socket.inet_aton(UDP_IP_ADDRESS)
    mreq = struct.pack('4s4s', group, socket.inet_aton(ip_addr))
    serverSock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    print("Starting on IP:", ip_addr)
    print("Multicast:", multicast_addr)

    # Set up Pygame stuff
    pygame.init()
    pygame.display.set_caption('Jack Cast')
    icon = pygame.image.load('GUI/jack_cast_icon.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    watching = True

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
