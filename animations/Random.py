import BaseAnimation
import random


class Random(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Random')
        self.shouldRun = True

        self.options = []

    def run(self):
        while self.shouldRun:
            self.pixels.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            self.pixels.show()

    def stop(self):
        self.shouldRun = False
