from BaseAnimation import BaseAnimation
import random

class Party(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Party')
        self.shouldRun = True

        self.options = []

    def run(self):
        while self.shouldRun:
            for i in range(self.numPixels):
                self.pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.pixels.show()

    def stop(self):
        self.shouldRun = False
