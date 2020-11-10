from Preferences import Preferences
from Logger import Logger
from website import Website
from ControllerManager import ControllerManager
from scenes import Scenes
from Hardware import Hardware

class LEDController:
    def __init__(self):
        self.logger = Logger()
        self.preferences = self.logger.get_preferences()
        self.website = Website(self.preferences)
        self.controller_manager = ControllerManager()
        self.scenes = Scenes()
        self.hardware = Hardware()



if __name__ == '__main__':
    ledcontroller = LEDController()

