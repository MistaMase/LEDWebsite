import threading
import time

class Strobe(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = "Strobe"
        self.pixels = pixels
        self.numPixels = numPixels

    def run(self):
        while self.shouldRun:
            self.pixels.fill((255,255,255))
            self.pixels.show()
            self.pixels.fill((0,0,0))
            self.pixels.show()

    def stop(self):
        self.shouldRun = False
