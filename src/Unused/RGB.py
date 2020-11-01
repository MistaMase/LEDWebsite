from BaseAnimation import BaseAnimation

class RGB(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'RGB')

    def run(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()
        for i in range(self.numPixels):
            if i % 3 == 0:
                self.pixels[i] = ((255,0,0))
            elif i % 3 == 1:
                self.pixels[i] = ((0,255,0))
            else:
                self.pixels[i] = ((0,0,255))
        self.pixels.show()

    def stop(self):
        pass
