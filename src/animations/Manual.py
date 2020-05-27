from BaseAnimation import BaseAnimation

class Manual(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Manual')
        self.colors = ((10, 20, 30))
        self.shouldRun = True
        self.shouldUpdate = True

        self.parameters = {
            'RValue': 0,
            'GValue': 0,
            'BValue': 0
        }

        # Editable options
        self.options = [
            ['Slider', 'RValue',  (0, 255, self.parameters['RValue'])],
            ['Slider', 'GValue', (0, 255, self.parameters['GValue'])],
            ['Slider', 'BValue', (0, 255, self.parameters['BValue'])]
        ]

    def getOptions(self):
        allOptions = super().getOptions()

        # Append user defined colors
        for key,value in self.preferences.get_color_preferences():
            allOptions.append(['UserColor', key, value])

        return allOptions

    def run(self):
        while self.shouldRun:
            if self.shouldUpdate:
                self.colors = (int(self.parameters['RValue']), int(self.parameters['GValue']), int(self.parameters['BValue']))
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
