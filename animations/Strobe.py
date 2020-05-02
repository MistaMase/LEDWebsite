import BaseAnimation
import time

class Strobe(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Strobe')
        self.shouldRun = True

        self.options = []

    def run(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()
        while self.shouldRun:
            self.pixels.fill((255,255,255))    
            self.pixels.show()
            time.sleep(0.05)
            self.pixels.fill((0,0,0))
            self.pixels.show()
            time.sleep(0.05)

    def stop(self):
        self.shouldRun = False
