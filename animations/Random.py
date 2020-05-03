from BaseAnimation import BaseAnimation
import random
import time


class Random(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Random')
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
            self.pixels.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.pixels.show()
            time.sleep(float(self.parameters['Sleep']))

    def stop(self):
        self.shouldRun = False
