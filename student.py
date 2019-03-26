from socket import socket
from zlib import decompress
from SocketBuilder import SocketObj
import pygame

WIDTH = 1920
HEIGHT = 1080


def recvall(conn, length):
    """ Retreive all pixels. """

    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf


def main():
    new_socket = SocketObj('127.0.0.1', 5000, 'client')
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    watching = True
    new_socket.sock.connect((new_socket.host, new_socket.port))
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break

            # Retrieve the size of the pixels length
            size_len = int.from_bytes(new_socket.sock.recv(1), byteorder='big')
            # Retrieve the pixels length
            PixelLength = int.from_bytes(new_socket.sock.recv(size_len), byteorder='big')
            # Retrieve the pixels
            pixels = decompress(recvall(new_socket.sock, PixelLength))
            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')

            # Display the picture
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)
    finally:
        new_socket.sock.close()


if __name__ == '__main__':
    main()
