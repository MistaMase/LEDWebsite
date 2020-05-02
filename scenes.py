# LED Light Imports
import board
import neopixel

# Dynamic Animation Imports
from pathlib import Path
import sys
import inspect
import pkgutil
from importlib import import_module
animations = []
animationNames = []
for (_, name, _) in pkgutil.iter_modules([Path('./animations')]):
    animations.append(import_module('animations.' + name, package=__name__))
    for i in dir(animations[len(animations)-1]):
        attribute = getattr(animations[len(animations)-1], i)
        for i in dir(animations[len(animations)-1]):
            attribute = getattr(animations[len(animations)-1], i)
            if inspect.isclass(attribute):
                setattr(sys.modules[__name__], name, attribute)


numPixels = 300


# Initializes the LED strip
pixels = neopixel.NeoPixel(board.D18, numPixels, brightness=0.7, auto_write=False, pixel_order=neopixel.GRB)

def getParameters():
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
        print("Shutdown " + thread.name)

# Parses the incoming LED command and calls the correct function
def changeMode(msg):
    global thread
    try:
        print('Attempting to start ' + msg)
        shutdownThread()
        createThread(msg)
        return True
    except:
        print('Failed to start ' + msg)
        return False
    return False


# Start up the lights in 'Off' Mode
populateAnimationNames()
thread = createThread('Off')


if __name__ == "__main__":
    try:
        while True:
            mode = input("Mode: ")
            parseInputMessage(mode)
    except (KeyboardInterrupt, SystemExit):
        thread = Off()
        while thread.isAlive():
            pass
        sys.exit()
