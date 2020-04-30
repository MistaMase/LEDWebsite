import board
import neopixel
import random
import threading
import sys
import time

numPixels = 300

# Initializes the LED strip
pixels = neopixel.NeoPixel(board.D18, numPixels, brightness=0.05, auto_write=False, pixel_order=neopixel.RGB)

class On(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = 'On'
        print(self.name)

    def run(self):
        pixels.fill((255,255,255))
        pixels.show()

    def stop(self):
        pass

class ManualColor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = 'Manual Color'
        print(self.name)
        self.colors = ((200, 200, 200))
        self.shouldRun = True

    def setColor(color):
        parsedColors = color.split
        self.newColors = (parsedColors[0], parsedColors[1], parsedColors[2])

    def run(self):
        while self.shouldRun:
            if self.newColors != self.colors:
                self.colors = self.newColors
                pixels.fill(self.colors)
                pixels.show()
            else:
                pass

    def stop(self):
        self.shouldRun = False

class Off(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = 'Off'
        print(self.name)

    def run(self):
        pixels.fill((0,0,0))
        pixels.show()

    def stop(self):
        pass

class RandomColor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = 'Random'
        self.shouldRun = True
        print(self.name)

    def run(self):
        while self.shouldRun:
            pixels.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            pixels.show()

    def stop(self):
        self.shouldRun = False

class PartyMode(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = 'Party'
        print(self.name)

    def run(self):
        while self.shouldRun:
            for i in range(numPixels):
                pixels[i] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            pixels.show()
            #time.sleep(0.1)

    def stop(self):
        self.shouldRun = False

class ScrollColor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = 'Scroll'
        self.margin = 10     # 2*Margin is scroll width

    def run(self):
        pixels.fill((0,0,0))
        pixels.show()
        while self.shouldRun:
            color = ((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            for i in range(-self.margin, numPixels + self.margin+1, 1):
                if self.shouldRun == False:
                    return
                for j in range(-self.margin, self.margin+1, 1):
                    if i+j >= 0 and i+j < numPixels:
                        pixels[i+j] = color
                if i-self.margin >= 0:
                    pixels[i-self.margin-1] = ((0,0,0))
                pixels.show()
                #time.sleep(0.1) No sleep necessary as Python is slow

    def stop(self):
        self.shouldRun = False

class Strobe(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.shouldRun = True
        self.name = "Strobe"

    def run(self):
        while self.shouldRun:
            for i in range(numPixels):
                pixels[i] = ((255,255,255))
            pixels.show()
            time.sleep(0.05)
            for i in range(numPixels):
                pixels[i] = ((0,0,0))
            pixels.show()
            time.sleep(0.05)

    def stop(self):
        self.shouldRun = False


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


def userInput():
    while True:
        mode = input("Mode: ")
        parseInputMessage(mode)

if __name__ == "__main__":
    try:
        userInput()
    except (KeyboardInterrupt, SystemExit):
        thread = Off()
        while thread.isAlive():
            pass
        sys.exit()
