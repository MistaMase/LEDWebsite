from BaseAnimation import BaseAnimation
import time
import letterlayout as layout

class VerticalScroll(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Q')
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
        # Set all pixels to black
        self.pixels.fill((0,0,0))

        while self.shouldRun:
            # Color the letter
            for row in range(len(layout.Q)):
                for col in range(len(layout.Q[row])) :
                    if layout.Q[row][col] != -1:
                        self.pixels[layout.Q[row][col]] = (255, 255, 255)
                self.pixels.show()
                time.sleep(float(self.parameters['Sleep']))

            # Black out the letter
            for row in range(len(layout.Q)):
                for col in range(len(layout.Q[row])) :
                    if layout.Q[row][col] != -1:
                        self.pixels[layout.Q[row][col]] = (0, 0, 0)
            self.pixels.show()

    def stop(self):
        self.shouldRun = False
