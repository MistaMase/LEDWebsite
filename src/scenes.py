# LED Light Imports
import board
import neopixel

# Inform the module of the globals
global logger


# Dynamic Animation Imports
from pathlib import Path
import sys
import inspect
import pkgutil
from importlib import import_module

# Dynamically imports all of the modules in the "animations" folder
# TODO Change This
animations = []
animationNames = []
for (_, name, _) in pkgutil.iter_modules([Path('/home/pi/LEDWebsite/src/animations')]):
    animations.append(import_module('animations.' + name, package=__name__))
    for i in dir(animations[len(animations)-1]):
        attribute = getattr(animations[len(animations)-1], i)
        for i in dir(animations[len(animations)-1]):
            attribute = getattr(animations[len(animations)-1], i)
            if inspect.isclass(attribute):
                setattr(sys.modules[__name__], name, attribute)


class Scenes:
    def __init__(self):
        # Informs this scope that there's a global preferences object
        global preferences

        # Define the number of pixels for the LED Strip
        self.numPixels = preferences.get_setup_preferences('num-pixels')

        # Initializes the LED strip
        self.pixels = neopixel.NeoPixel(board.D18, self.numPixels, brightness=preferences.get_setup_preferences('brightness'),
                                        auto_write=False, pixel_order=neopixel.GRB)

        # TODO Change this
        # Populate the animation names
        self.populate_animation_names()

        # Easy reference to the current running animation
        self.thread = self.create_thread('Off')

    def get_animation_options(self):
        return self.thread.getOptions()

    def get_animation_names(self):
        try:
            return animationNames
        except:
            return None

    # TODO Change this
    # Populates the animationNames array which contains all the dynamically imported animations' names
    def populate_animation_names(self):
        global animationNames, animations
        for a in range(len(animations)):
            animationNames.append(animations[a].__name__.split('.')[1])

    # If the string name exists, a new animation thread is created and the animation is started
    def create_thread(self, name):
        global animationNames
        try:
            for a in range(len(animationNames)):
                if animationNames[a] == name:
                    threadClass = globals()[animationNames[a]]
                    self.thread = threadClass(self.pixels, self.numPixels)
                    self.thread.start()
                    return self.thread
            return None
        except:
            return None

    # Turns off the current animation thread
    def shutdown_thread(self):
        if self.thread.isAlive():
            self.thread.stop()
            while self.thread.isAlive():
                pass
            logger.log('Scenes', f'Shutdown {self.thread.name}')

    # Parses the incoming LED command and calls the correct function
    def change_mode(self, msg):
        try:
            logger.log('Website', f'Attempting to start {msg}')
            self.shutdown_thread()
            self.create_thread(msg)
            return True
        except:
            logger.log('Website', f'Failed to start {msg}')
            return False
        return False

    def get_thread_name(self):
        return self.thread.name

