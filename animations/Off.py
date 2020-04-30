import threading

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
