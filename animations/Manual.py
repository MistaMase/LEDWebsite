from BaseAnimation import BaseAnimation

class Manual(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Manual Color')
        self.colors = ((0,0,0))
        self.shouldRun = True
        self.shouldUpdate = True

        self.parameters = {
            'RValue': 0,
            'GValue': 0,
            'BValue': 0
        }

        # Editable options
        self.options = [
            ['Slider', 'RValue',  (0, 255, self.colors[0])],
            ['Slider', 'GValue', (0, 255, self.colors[1])],
            ['Slider', 'BValue', (0, 255, self.colors[2])]
        ]

    def setColor(self, color):
        parsedColors = color.split()
        self.newColors = (int(parsedColors[0]), int(parsedColors[1]), int(parsedColors[2]))

    def run(self):
        while self.shouldRun:
            if self.shouldUpdate:
                print("New Color")
                self.colors = (self.parameters['RValue'], self.parameters['GValue'], self.parameters['BValue'])
                self.pixels.fill(self.colors)
                self.pixels.show()
                self.shouldUpdate = False
            else:
                pass

    def stop(self):
        self.shouldRun = False

    def setParameter(self, param):
        super().setParameter(param)
        self.shouldUpdate = True
