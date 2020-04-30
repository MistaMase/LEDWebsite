import board
import neopixel
import random
import threading
import sys
import time

numPixels = 300

# Initializes the LED strip
pixels = neopixel.NeoPixel(board.D18, numPixels, brightness=0.5, auto_write=False, pixel_order=neopixel.GRB)


# Parses the incoming LED command and calls the correct function
#def parseInputMessage(client, userdata, msg):
def parseInputMessage(msg):
    #msg = str(msg.payload, 'utf-8')
    print("Message: " + msg)
    global thread
    if msg == 'ON':
        print("Turning Lights On")
        if thread.isAlive():
            thread.stop()
            print("Shutdown " + thread.name)
        thread = On()
        thread.start()
        return True
    elif msg == 'OFF':
        print("Turning Lights Off")
        if thread.isAlive():
            thread.stop()
            print("Shutdown " + thread.name)
        thread = Off()
        thread.start()
        return True
    elif msg == 'RANDOM':
        print('Setting Lights To Random Color')
        if thread.isAlive():
            thread.stop()
            print("Shutdown " + thread.name)
        thread = RandomColor()
        thread.start()
        return True
    elif msg == 'PARTY':
        print("Party Mode")
        if thread.isAlive():
            thread.stop()
            print("Shutdown " + thread.name)
        thread = PartyMode()
        thread.start()
        return True
    elif msg == 'SCROLL':
        print("Scrolling LEDs")
        if thread.isAlive():
            thread.stop()
            print("Shutdown " + thread.name)
        thread = ScrollColor()
        thread.start()
        return True
    elif msg == 'STROBE':
        print("Strobing")
        if thread.isAlive():
            thread.stop()
            print("Shutdown " + thread.name)
        thread = Strobe()
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
