import threading
import random
import time

class Pyramid(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = 'Pyramid'
        self.pixels = pixels
        self.numPixels = numPixels

    def run(self):
        while self.shouldRun:
            self.pixels.fill((0,0,0))
            self.pixels.show()
            middle = int(self.numPixels / 2)
            for i in range(middle):
                color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                if self.shouldRun == False:
                    return
                for j in range(i):
                    self.pixels[middle + j] = color
                    self.pixels[middle - j] = color
                self.pixels.show()
                time.sleep(0.01)


    def stop(self):
        self.shouldRun = False
