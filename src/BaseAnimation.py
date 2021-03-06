import threading
from Preferences import Preferences
from abc import ABC, abstractmethod


# Defines the base class for all animations to extend
# Format: DisplayType, DisplayName, Parameters
# DisplayType Parameters:
#   Slider:         minValue, maxValue, currentValue
#   UserColor:      tuple(colors)
class BaseAnimation(threading.Thread, ABC):
    def __init__(self, pixels, numPixels, name):
        threading.Thread.__init__(self)
        self.preferences = Preferences()
        self.pixels = pixels
        self.numPixels = numPixels
        self.name = name

    def getOptions(self):
        try:
            if self.options is not None:
                return self.options
            else:
                return []
        except:
            return []

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def setParameter(self, param):
        if self.parameters is not None:
            if param[0] in self.parameters:
                self.parameters[param[0]] = param[1]
