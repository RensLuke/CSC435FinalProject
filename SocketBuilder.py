from screenshot import ScreenShotObj
from SendScreenShots import SendScreenShotObj
from threading import Thread
import socket
from zlib import decompress
import contextlib
with contextlib.redirect_stdout(None):
    import pygame


class SocketObj:
    def __init__(self, host, port, socket_type):
        self.sock = socket.socket()
        self.host = host
        self.port = port
        if socket_type == 'server':
            self.sock.bind((self.host, self.port))
        elif socket_type == 'client':
            pass

    def recvall(self, conn, length):
        """ Retreive all pixels. """

        buf = b''
        while len(buf) < length:
            data = conn.recv(length - len(buf))
            if not data:
                return
            buf += data
        return buf

    def client_connection(self, WIDTH, HEIGHT):
        self.is_not_used()
        while True:
            try:
                self.sock.connect((self.host, self.port))
                print("Connection Established")
                break
            except ConnectionRefusedError:
                print("Looking for connection...")

        pygame.init()
        pygame.display.set_caption('Rolt VNC')
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        watching = True

        try:
            while watching:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        watching = False
                        break

                # Retrieve the size of the pixels length
                size_len = int.from_bytes(self.sock.recv(1), byteorder='big')
                # Retrieve the pixels length
                PixelLength = int.from_bytes(self.sock.recv(size_len), byteorder='big')
                # Retrieve the pixels
                pixels = decompress(self.recvall(self.sock, PixelLength))
                # Create the Surface from raw pixels
                img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')

                # Display the picture
                screen.blit(img, (0, 0))
                pygame.display.flip()
                clock.tick(60)
        finally:
            self.sock.close()

    def server_connection(self):
        self.is_not_used()
        try:
            self.sock.listen(5)
            print('Server started.')
            while 'connected':
                try:
                    client_conn, client_addr = self.sock.accept()
                except OSError:
                    print("Connection was aborted")
                    break
                print('Client connected IP:', client_addr)
                SS = ScreenShotObj()
                new_video_stream = SendScreenShotObj(client_conn, SS)
                try:
                    thread = Thread(target=new_video_stream.send())
                    thread.start()
                except ConnectionAbortedError:
                    print("Connection was aborted")
                    break
        finally:
            self.sock.close()

    def is_not_used(self):
        pass





