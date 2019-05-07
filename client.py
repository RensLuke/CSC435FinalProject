import zlib
import socket
import struct
import helper
import pygame

# Set defaults
network = helper.NetworkingObj()
ip_addr = network.get_sfa_ip()
multicast_addr = '239.1.1.1'
resolution = '1600 x 900'


def run_me(pIP, pMulti, pRes, pSaved):
    global ip_addr, multicast_addr, resolution
    if pSaved:
        ip_addr = pIP
        multicast_addr = pMulti
        resolution = pRes
    start()


def start():
    # Declaring variables
    global ip_addr, multicast_addr, resolution
    UDP_IP_ADDRESS = multicast_addr
    UDP_PORT_NO = 6789
    server_address = ('', UDP_PORT_NO)
    resolution = resolution.split()
    width = int(resolution[0])
    height = int(resolution[2])
    
    # Declaring error checking variables
    OSErrorCount = 0
    CompressionErrorCount = 0
    pygameErrorCount = 0
    successCounter = 0

    # Setting up sockets
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # declaring UDP socket
    serverSock.bind(server_address)  # binding the port number to the port
    serverSock.settimeout(5)  # setting socket timeout for 5 seconds
    mreq = struct.pack('4s4s', socket.inet_aton(UDP_IP_ADDRESS), socket.inet_aton(ip_addr))  # declaring struck w/ local IP and Multicast address in it
    serverSock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)  # setting socket to accept multicast packets from group to local address
    print("Starting on IP:", ip_addr)
    print("Multicast:", multicast_addr)
    print(width, height)

    # Pygame setup
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
                # handle for pygame exit
                if event.type == pygame.QUIT:
                    watching = False
                    pygame.quit()
                    break
                 # handle for pygame resize
                elif event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)  # adjusting screen size
                    width2 = event.dict['size'][0]  # grabbing new width
                    height2 = event.dict['size'][1]  # grabbing new height
            else:
                try:
                    data, addr = serverSock.recvfrom(32)  # receive number of chunks to put together
                    num = data.decode('utf-8')
                except socket.timeout:  # detection for a socket timeout
                    pygame.quit()
                    break
                except OSError:  # detection for if a 64k chunk is read
                    OSErrorCount += 1
                else:
                    chunk = b''
                    for j in range(int(num)):  # reassembling chunks into screen shot
                        data, addr = serverSock.recvfrom(64000)
                        chunk = chunk + data
                    try:  # decompressing the screen shot
                        zobj = zlib.decompressobj()
                        pixels = zobj.decompress(chunk)
                    except zlib.error:  # detection if chunks assembled out of order
                        CompressionErrorCount += 1
                    else:
                        # Create the Surface from raw pixels
                        try:  # Create the Surface from raw pixels
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


