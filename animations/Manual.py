import threading

class Manual(threading.Thread):
    def __init__(self, pixels, numPixels):
        threading.Thread.__init__(self)
        self.name = 'Manual Color'
        self.colors = ((0,0,0))
        self.newColors = ((200, 200, 200))
        self.pixels = pixels
        self.numPixels = numPixels
        self.shouldRun = True

    def setColor(self, color):
        parsedColors = color.split()
        self.newColors = (int(parsedColors[0]), int(parsedColors[1]), int(parsedColors[2]))

    def run(self):
        while self.shouldRun:
            if self.newColors != self.colors:
                print("New Color")
                self.colors = self.newColors
                self.pixels.fill(self.colors)
                self.pixels.show()
            else:
                pass

    def stop(self):
        self.shouldRun = False
