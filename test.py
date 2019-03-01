import time
import cv2
import mss
import numpy
import socket
from io import StringIO

# using loop back address and port 5000
host = "144.96.33.160"
port = 80

# initializing socket object
s = socket.socket()

# binding loop back address and port to socket
# s.connect((host, port))

# in 1 minute 30 seconds 700kb of data was generated, for 15 users makes 116kb/s 
with mss.mss() as sct:
    with open("data.txt", 'w') as f:
        # Part of the screen to capture
        monitor = {'top': 40, 'left': 0, 'width': 800, 'height': 400}

        while 'Screen capturing':

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.ndarray(sct.grab(monitor))
            # print(str(img))

            a = StringIO()
            numpy.savez_compressed(a, frame=img)
            a.seek(0)
            out = a.read()
            s.sendall(out)

            # print(type(img))
            # data = s.recv(1024).decode('utf-8')

            # f.write(str(img))

            # Display the picture
            cv2.imshow('OpenCV/Numpy normal', img)

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

