from BaseAnimation import BaseAnimation
import random

class Party(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Party')
        self.shouldRun = True

        # Internal settings for the possible options
        self.parameters = {
            'Sleep': 0.0
        }

        # Options returned by the website
        self.options = [
            ['Slider', 'Sleep', (0, 1, self.parameters['Sleep'])]
        ]

    def run(self):
        while self.shouldRun:
            for i in range(self.numPixels):
                self.pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.pixels.show()
            time.sleep(float(self.parameters['Sleep']))

    def stop(self):
        self.shouldRun = False
