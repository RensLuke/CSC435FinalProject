import socket
import sys
import cv2
import mss
import numpy as np
from io import StringIO

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.197', 80)
print('Starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)
raw = []

while True:
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)
        ultimate_buffer=''
        while True:
            receiving_buffer = connection.recv(1024)
            if not receiving_buffer: break
            ultimate_buffer+= receiving_buffer
            print('-')
        final_image=np.load(StringIO(ultimate_buffer))['frame']
        cv2.imshow('openCV/Numpy normal', final_image)
    finally:
        connection.close()
