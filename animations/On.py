import BaseAnimation


class On(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'On')
        self.options = []

    def run(self):
        self.pixels.fill((255,255,255))
        self.pixels.show()

    def stop(self):
        pass
