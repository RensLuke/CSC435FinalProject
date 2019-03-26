from zlib import compress
from mss import mss


class ScreenShotObj:
    def __init__(self):
        pass

    def takescreenshot(self):
        self.is_not_used()
        sct = mss()
        rect = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
        img = sct.grab(rect)
        return compress(img.rgb, 6)

    def is_not_used(self):
        pass
