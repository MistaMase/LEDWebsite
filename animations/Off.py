import threading

class Off(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.name = 'Off'
        self.pixels = pixels
        self.numPixels = numPixels

    def run(self):
        pixels.fill((0,0,0))
        pixels.show()

    def stop(self):
        pass
