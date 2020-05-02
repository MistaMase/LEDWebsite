import threading

class Off(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.name = 'Off'
        self.pixels = pixels
        self.numPixels = numPixels

        # Editable options
        self.options = {}

    def getOptions(self):
        return self.options

    def run(self):
        self.pixels.fill((0,0,0))
        self.pixels.show()

    def stop(self):
        pass
