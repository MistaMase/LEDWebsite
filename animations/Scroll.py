from BaseAnimation import BaseAnimation
import random

class Scroll(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Scroll')
        self.shouldRun = True

        # Internal settings for the possible options
        self.parameters = {
            'Margin': 10
        }

        # Options returned by the website
        self.options = [
            ['Slider', 'Margin', (0, int(numPixels/2), 10)]
        ]

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

