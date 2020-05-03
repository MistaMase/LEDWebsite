import threading
from abc import ABC, abstractmethod


class BaseAnimation(threading.Thread, ABC):
    def __init__(self, pixels, numPixels, name):
        threading.Thread.__init__(self)
        self.pixels = pixels
        self.numPixels = numPixels
        self.name = name

    def getOptions(self):
        if self.options is not None:
            return self.options
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
