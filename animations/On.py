import threading

class On(threading.Thread):
    def __init__(self, pixels):
        threading.Thread.__init__(self)
        self.name = 'On'
        self.pixels = pixels

    def run(self):
        pixels.fill((255,255,255))
        pixels.show()

    def stop(self):
        pass
