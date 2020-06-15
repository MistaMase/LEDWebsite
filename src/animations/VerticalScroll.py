from BaseAnimation import BaseAnimation
import time
import letterlayout as layout

class VerticalScroll(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'VerticalScroll')
        self.shouldRun = True

        # Internal settings for the possible options
        self.parameters = {
            'Sleep': 1.0
        }

        # Options returned by the website
        self.options = [
            ['Slider', 'Sleep', (0, 1, self.parameters['Sleep'])]
        ]

    def run(self):
        while self.shouldRun:
            # Color the letter
            for row in range(len(layout.I)):
                for col in range(len(layout.I[row])) :
                    if layout.I[row][col] != -1:
                        self.pixels[112 + layout.I[row][col]] = (255, 255, 255)
                self.pixels.show()
                time.sleep(float(self.parameters['Sleep']))

            # Black out the letter
            for row in range(len(layout.I)):
                for col in range(len(layout.I[row])) :
                    if layout.I[row][col] != -1:
                        self.pixels[112 + layout.I[row][col]] = (0, 0, 0)
                self.pixels.show()

    def stop(self):
        self.shouldRun = False
