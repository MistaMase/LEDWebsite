from BaseAnimation import BaseAnimation
import random
import time
import math

class Fade(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Fade')
        self.shouldRun = True

        # Internal settings for the possible options
        self.parameters = {
            'Sleep': 0.01,
            'Steps': 10
        }

        # Options returned by the website
        self.options = [
            ['Slider', 'Sleep', (0, 1, self.parameters['Sleep'])],
            ['Slider', 'Steps', (2, 50, self.parameters['Steps'])]
        ]

    def run(self):
        while self.shouldRun:
            self.pixels.fill((0,0,0))
            self.pixels.show()
            color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            rstep = color[0] / float(self.parameters['Steps'])
            gstep = color[1] / float(self.parameters['Steps'])
            bstep = color[2] / float(self.parameters['Steps'])
            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(float(self.parameters['Sleep']))
            for step in range(int(self.parameters['Steps'])):
                color = ((math.ceil(color[0] - rstep), math.ceil(color[1] - gstep), math.ceil(color[2] - bstep)))
                self.pixels.fill(color)
                self.pixels.show()
                time.sleep(float(self.parameters['Sleep']))

    def stop(self):
        self.shouldRun = False
