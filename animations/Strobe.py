import threading

class Strobe(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = "Strobe"
        self.pixels = pixels
        self.numPixels = numPixels

    def run(self):
        while self.shouldRun:
            for i in range(self.numPixels):
                pixels[i] = ((255,255,255))
            pixels.show()
            time.sleep(0.05)
            for i in range(self.numPixels):
                pixels[i] = ((0,0,0))
            pixels.show()
            time.sleep(0.05)

    def stop(self):
        self.shouldRun = False
