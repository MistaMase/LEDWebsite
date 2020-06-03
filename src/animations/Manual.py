from BaseAnimation import BaseAnimation

class Manual(BaseAnimation):
    def __init__(self, pixels, numPixels):
        super().__init__(pixels, numPixels, 'Manual')
        self.colors = ((0, 0, 0))
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

    # Override the BaseAnimations method to return color profiles also
    def getOptions(self):
        # Get the actual options
        options = super().getOptions().copy()

       # Append the color profile options
        for color in self.preferences.get_color_preferences().keys():
            options.append(['UserColor', color])
        print("OPTIONS")
        print(options)
        return options


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
        if param[0] == 'UserColor':
            if param[1] in self.preferences.get_color_preferences().keys():
                super().setParameter('RValue', self.preferences.get_color_preferences(key=param)[0])
                super().setParameter('GValue', self.preferences.get_color_preferences(key=param)[1])
                super().setParameter('BValue', self.preferences.get_color_preferences(key=param)[2])
            else:
                if self.preferences.get_debug_preferences('scenes-debug'):
                    print('Scenes Debug: Error finding user color ' + str(param[1]))
        else:
            super().setParameter(param)
        self.shouldUpdate = True
