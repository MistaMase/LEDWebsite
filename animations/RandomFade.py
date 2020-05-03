from BaseAnimation import BaseAnimation
import random
import time

class RandomFade(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'RandomFade')
        self.shouldRun = True

    def run(self):
        middle = int(self.numPixels / 2)
        current = middle
        self.pixels.fill((0,0,0))
        self.pixels.show()
        while self.shouldRun:
            nextPosition = random.randint(0, middle)
            color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            for i in range(abs(current - nextPosition)):
                if self.shouldRun == False:
                    return
                for j in range(i):
                    self.pixels[current + j] = color
                    self.pixels[current - j] = color
                self.pixels.show()
                time.sleep(0.01)
            current = nextPosition


    def stop(self):
        self.shouldRun = False
