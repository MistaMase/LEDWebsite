from BaseAnimation import BaseAnimation
import random
import time

class Pyramid(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Pyramid')
        self.shouldRun = True

        # Internal settings for the possible options
        self.parameters = {
            'Sleep': 0.01
        }

        # Options returned by the website
        self.options = [
            ['Slider', 'Sleep', (0, 1, self.parameters['Sleep'])]
        ]

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
                time.sleep(self.parameters['Sleep'])


    def stop(self):
        self.shouldRun = False
