import threading

class Scroll(threading.Thread):
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
