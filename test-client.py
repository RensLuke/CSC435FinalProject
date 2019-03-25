import socket
from threading import Thread
from zlib import compress
from mss import mss


def connection(client_conn):
    while 'recording':
        pixels = retrieve_screen_shot()

        pixel_length = len(pixels)
        size_len = (pixel_length.bit_length() + 7) // 8

        # Send the size of the pixels length
        try:
            client_conn.send(bytes([size_len]))
        except ConnectionResetError:
            print("Connection Terminated")
            break

        # Send the actual pixels length
        size_bytes = pixel_length.to_bytes(size_len, 'big')
        try:
            client_conn.send(size_bytes)
        except ConnectionResetError:
            print("connection Terminated")
        

        # Send pixels
        try:
            client_conn.sendall(pixels)
        except ConnectionResetError:
            print("connection Terminated")
            break


def retrieve_screen_shot():
    sct = mss()
    rect = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
    img = sct.grab(rect)
    return compress(img.rgb, 6)


def main():
    host = '127.0.0.1'
    port = 5000
    sock = socket.socket()
    sock.bind((host, port))
    try:
        sock.listen(5)
        print('Server started.')

        while 'connected':
            client_conn, client_addr = sock.accept()
            print('Client connected IP:', client_addr)
            thread = Thread(target=connection, args=(client_conn,))
            thread.start()
    finally:
        sock.close()


if __name__ == '__main__':
    main()


