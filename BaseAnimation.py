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
        else:
            raise NotImplementedError

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass
