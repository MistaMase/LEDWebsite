import threading

class Party(threading.Thread):
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
