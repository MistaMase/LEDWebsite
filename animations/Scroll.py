from BaseAnimation import BaseAnimation
import random

class Scroll(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Scroll')
        self.shouldRun = True

        # Internal settings for the possible options
        self.parameters = {
            'Margin': 10,
            'Sleep': 0.0
        }

        # Options returned by the website
        self.options = [
            ['Slider', 'Margin', (0, int(numPixels/2), 10)],
            ['Slider', 'Sleep', (0, 1, self.parameters['Sleep'])]
        ]

    def run(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()
        while self.shouldRun:
            color = ((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            for i in range(-int(self.parameters['Margin']), self.numPixels + int(self.parameters['Margin'])+1, 1):
                self.pixels.fill((0,0,0))
                if self.shouldRun == False:
                    return
                for j in range(-int(self.parameters['Margin']), int(self.parameters['Margin'])+1, 1):
                    if i+j >= 0 and i+j < self.numPixels:
                        self.pixels[i+j] = color
                self.pixels.show()
                time.sleep(self.parameters['Sleep'])

    def stop(self):
        self.shouldRun = False

