import threading
import random

class Party(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = 'Party'
        self.pixels = pixels
        self.numPixels = numPixels

    def run(self):
        while self.shouldRun:
            for i in range(self.numPixels):
                self.pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.pixels.show()

    def stop(self):
        self.shouldRun = False
