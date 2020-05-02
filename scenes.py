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
    print(thread.name)
    print("Thread options")
    print(thread.getOptions())
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
        print("Animation Names size")
        print(len(animationNames))
        for a in range(len(animationNames)):
            print(animationNames[a])
            if animationNames[a] == name:
                threadClass = globals()[animationNames[a]]
                print('Threaded Class')
                print(threadClass)
                thread = threadClass(pixels, numPixels)
                print("1")
                thread.start()
                print('2')
                return thread
        return None
    except Exception as e:
        print(e)
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
    print("Message: " + msg)
    global thread
    if msg == 'On':
        try:
            print("Turning Lights On")
            shutdownThread()
            createThread('On')
            return True
        except:
            print("Failed to start On")
            return False
    elif msg == 'Off':
        try:
            print("Turning Lights Off")
            shutdownThread()
            createThread('Off')
            return True
        except:
            print("Failed to start Off")
            return False
    elif msg == 'Random':
        try:
            print('Random Mode')
            shutdownThread()
            createThread('Random')
            return True
        except:
            print("Failed to start Random")
            return False
    elif msg == 'Party':
        try:
            print("Party Mode")
            shutdownThread()
            createThread('Party')
            return True
        except:
            print("Failed to start Party")
            return False
    elif msg == 'Scroll':
        try:
            print("Scroll Mode")
            shutdownThread()
            createThread('Scroll')
            return True
        except:
            print("Failed to start Scroll")
            return False
    elif msg == 'Strobe':
        try:
            print("Strobe Mode")
            shutdownThread()
            createThread('Strobe')
            return True
        except:
            print("Failed to start Strobe")
            return False
    elif msg == 'Manual':
        try:
            print("Manual Mode")
            shutdownThread()
            createThread('Manual')
            return True
        except:
            print("Failed to start Manual")
            return False
    elif msg == 'Pyramid':
        try:
            print('Pyramid Mode')
            shutdownThread()
            createThread('Pyramid')
            return True
        except:
            print("Failed to start Pyramid")
            return False
    elif msg == 'RandomThicc':
        try:
            print("Random Thicc Mode")
            shutdownThread()
            createThread('RandomThicc')
            return True
        except:
            print("Failed to start Random Thicc")
            return False
    elif msg == "RandomFade":
        try:
            print("Random Fade Mode")
            shutdownThread()
            createThread('RandomFade')
            return True
        except:
            print("Failed to start Random Fade")
            return False
    elif msg == "RGB":
        try:
            print("RGB Mode")
            shutdownThread()
            createThread('RGB')
            return True
        except:
            print("Failed to start RGB Mode")
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
