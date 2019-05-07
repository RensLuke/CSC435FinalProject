from zlib import compress
import mss
import socket


class ScreenShotObj:
    def __init__(self):
        pass

    def takescreenshot(self, pWidth, pHeight):
        self.is_not_used()
        with mss.mss() as sct:
            rect = {'top': 0, 'left': 0, 'width': pWidth, 'height': pHeight}
            img = sct.grab(rect)
            return compress(img.rgb, 7)

    def is_not_used(self):
        pass


class NetworkingObj:
    def __init__(self):
        pass

    def get_sfa_ip(self):
        ipList = socket.gethostbyname_ex(socket.gethostname())[2]
        for x in range(len(ipList)):
            if '144.96' in ipList[x]:
                return ipList[x]

