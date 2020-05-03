from BaseAnimation import BaseAnimation
import time

class Strobe(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Strobe')
        self.shouldRun = True

        # Internal settings for the possible options
        self.parameters = {
            'RValue': 255,
            'GValue': 255,
            'BValue': 255,
            'Sleep': 0.05
        }

        # Options returned by the website
        self.options = [
            ['Slider', 'RValue', (0, 255, self.parameters['RValue'])],
            ['Slider', 'GValue', (0, 255, self.parameters['GValue'])],
            ['Slider', 'BValue', (0, 255, self.parameters['BValue'])],
            ['Slider', 'Sleep', (0, 0.2, self.parameters['Sleep'])]

        ]

    def run(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
        while self.shouldRun:
            self.pixels.fill((int(self.parameters['RValue']), int(self.parameters['GValue']), int(self.parameters['BValue'])))
            self.pixels.show()
            time.sleep(float(self.parameters['Sleep']))
            self.pixels.fill((0, 0, 0))
            self.pixels.show()
            time.sleep(float(self.parameters['Sleep']))

    def stop(self):
        self.shouldRun = False
