from BaseAnimation import BaseAnimation


class Off(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Off')

    def run(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()

    def stop(self):
        pass
