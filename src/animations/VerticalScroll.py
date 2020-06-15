from BaseAnimation import BaseAnimation
import time
import letterlayout as layout

class VerticalScroll(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'VerticalScroll')
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
            for row in range(len(layout.I)):
                for col in range(len(layout.I[row])) :
                    self.pixels[row][col] = (255, 255, 255)
                self.pixels.show()
                time.sleep(float(self.parameters['Sleep']))

    def stop(self):
        self.shouldRun = False
