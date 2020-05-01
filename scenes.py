import board
import neopixel

from animations.On import On
from animations.Off import Off
from animations.Random import Random
from animations.Party import Party
from animations.Scroll import Scroll
from animations.Strobe import Strobe
from animations.Manual import Manual

numPixels = 300

# Initializes the LED strip
pixels = neopixel.NeoPixel(board.D18, numPixels, brightness=0.7, auto_write=False, pixel_order=neopixel.GRB)

thread = Off(pixels, numPixels)
thread.start()

def shutdownThread():
    global thread
    if thread.isAlive():
        thread.stop()
        print("Shutdown " + thread.name)

# Parses the incoming LED command and calls the correct function
def changeMode(msg):
    global thread
    print("Message: " + msg)
    global thread
    if msg == 'On':
        print("Turning Lights On")
        shutdownThread()
        thread = On(pixels, numPixels)
        thread.start()
        return True
    elif msg == 'Off':
        print("Turning Lights Off")
        shutdownThread()
        thread = Off(pixels, numPixels)
        thread.start()
        return True
    elif msg == 'Random':
        print('Random Mode')
        shutdownThread()
        thread = Random(pixels, numPixels)
        thread.start()
        return True
    elif msg == 'Party':
        print("Party Mode")
        shutdownThread()
        thread = Party(pixels, numPixels)
        thread.start()
        return True
    elif msg == 'Scroll':
        print("Scroll Mode")
        shutdownThread()
        thread = Scroll(pixels, numPixels)
        thread.start()
        return True
    elif msg == 'Strobe':
        print("Strobe Mode")
        shutdownThread()
        thread = Strobe(pixels, numPixels)
        thread.start()
        return True
    elif msg == 'Manual':
        print("Manual Mode")
        shutdownThread()
        thread = Manual(pixels, numPixels)
        thread.start()
        return True
    return False


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
