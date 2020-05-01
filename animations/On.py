import threading

class On(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.name = 'On'
        self.pixels = pixels
        self.numPixels = numPixels

    def run(self):
        self.pixels.fill((255,255,255))
        self.pixels.show()

    def stop(self):
        pass
