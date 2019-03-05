import cv2
import mss
import numpy
import socket


def screenrecord():
    host = "127.0.0.1"
    port = 5000
    s = socket.socket()
    s.connect((host, port))

    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

        while "Screen capturing":

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))
            hold = str(img.tostring())
            s.send(hold.encode('utf-8'))
            # Display the picture
            # cv2.imshow("OpenCV/Numpy normal", img)

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break


def senddata():
    host = "144.96.33.160"
    port = 80
    s = socket.socket()
    s.connect((host, port))

    data = s.recv(1024).decode('utf-8')


screenrecord()


