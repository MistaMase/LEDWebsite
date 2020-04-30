import threading
import random

class Random(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.name = 'Random'
        self.shouldRun = True
        self.pixels = pixels
        self.numPixels = numPixels

    def run(self):
        while self.shouldRun:
            pixels.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            pixels.show()

    def stop(self):
        self.shouldRun = False
