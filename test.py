import time
import cv2
import mss
import numpy

# in 1 minute 30 seconds 700kb of data was generated, for 15 users makes 116kb/s 
with mss.mss() as sct:
    with open("data.txt", 'w') as f:
        # Part of the screen to capture
        monitor = {'top': 40, 'left': 0, 'width': 1980, 'height': 1800}

        while 'Screen capturing':

            # Get raw pixels from the screen, save it to a Numpy array
            img = numpy.array(sct.grab(monitor))
            f.write(str(img))
            # Display the picture
            cv2.imshow('OpenCV/Numpy normal', img)

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

