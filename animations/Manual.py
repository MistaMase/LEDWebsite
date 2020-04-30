class ManualColor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = 'Manual Color'
        print(self.name)
        self.colors = ((0,0,0))
        self.newColors = ((200, 200, 200))
        self.shouldRun = True

    def setColor(self, color):
        parsedColors = color.split()
        self.newColors = (int(parsedColors[0]), int(parsedColors[1]), int(parsedColors[2]))

    def run(self):
        while self.shouldRun:
            if self.newColors != self.colors:
                print("New Color")
                self.colors = self.newColors
                pixels.fill(self.colors)
                pixels.show()
            else:
                pass

    def stop(self):
        self.shouldRun = False