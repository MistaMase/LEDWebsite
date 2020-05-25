# LED Light Imports
import board
import neopixel

# User Preferences
import Preferences

# Dynamic Animation Imports
from pathlib import Path
import sys
import inspect
import pkgutil
from importlib import import_module
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

# Set up the preferences class
preferences = Preferences()

# Define the number of pixels for the LED Strip
numPixels = preferences.get_setup_preferences('num-pixels')

# Initializes the LED strip
pixels = neopixel.NeoPixel(board.D18, numPixels, brightness=preferences.get_setup_preferences('brightness'), auto_write=False, pixel_order=neopixel.GRB)

def getAnimationOptions():
    global thread
    return thread.getOptions()

def getAnimationNames():
    try:
        return animationNames
    except:
        return None

# Populates the animationNames array which contains all the dynamically imported animations' names
def populateAnimationNames():
    global animationNames, animations
    for a in range(len(animations)):
        animationNames.append(animations[a].__name__.split('.')[1])

# If the string name exists, a new animation thread is created and the animation is started
def createThread(name):
    global thread, animationNames
    try:
        for a in range(len(animationNames)):
            if animationNames[a] == name:
                threadClass = globals()[animationNames[a]]
                if name == 'Manual':
                    thread = threadClass(pixels, numPixels, params=preferences.get_color_preferences())
                else:
                    thread = threadClass(pixels, numPixels)
                thread.start()
                return thread
        return None
    except:
        return None

# Turns off the current animation thread
def shutdownThread():
    global thread
    if thread.isAlive():
        thread.stop()
        while thread.isAlive():
            pass
        if preferences.get_debug_preferences('scenes-debug'):
            print("Shutdown " + thread.name)

# Parses the incoming LED command and calls the correct function
def changeMode(msg):
    global thread
    try:
        if preferences.get_debug_preferences('scenes-debug'):
            print('Attempting to start ' + msg)
        shutdownThread()
        createThread(msg)
        return True
    except:
        if preferences.get_debug_preferences('scenes-debug'):
            print('Failed to start ' + msg)
        return False
    return False


# Start up the lights in 'Off' Mode
populateAnimationNames()
thread = createThread('Off')