import threading

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
