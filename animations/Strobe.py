import threading

class Strobe(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = "Strobe"

    def run(self):
        while self.shouldRun:
            for i in range(numPixels):
                pixels[i] = ((255,255,255))
            pixels.show()
            time.sleep(0.05)
            for i in range(numPixels):
                pixels[i] = ((0,0,0))
            pixels.show()
            time.sleep(0.05)

    def stop(self):
        self.shouldRun = False
