from Preferences import Preferences
from Logger import Logger
from website import Website
from ControllerManager import ControllerManager
from scenes import Scenes
from Hardware import Hardware

# Make Preferences free to use for everyone (Yes, it's programming communism)
logger = Logger()
preferences = Preferences()
website = Website()
controller_manager = ControllerManager()
scenes = Scenes()
hardware = Hardware()

if __name__ == '__main__':
    pass

