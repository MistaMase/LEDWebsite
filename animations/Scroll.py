import threading
import random

class Scroll(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = 'Scroll'
        self.margin = 10     # 2*Margin is scroll width
        self.pixels = pixels
        self.numPixels = numPixels

    def run(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()
        while self.shouldRun:
            color = ((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            for i in range(-self.margin, self.numPixels + self.margin+1, 1):
                if self.shouldRun == False:
                    return
                for j in range(-self.margin, self.margin+1, 1):
                    if i+j >= 0 and i+j < self.numPixels:
                        self.pixels[i+j] = color
                if i-self.margin >= 0:
                    self.pixels[i-self.margin-1] = ((0,0,0))
                self.pixels.show()

    def stop(self):
        self.shouldRun = False
