from time import time
from gui.display.display import Display


class Timer(Display):
    def __init__(self, root):
        super().__init__(root)
        self.reset()

    def start(self):
        self.t = time()
        self.running = True
        self.label.after(1000, self.update)

    def stop(self):
        self.running = False

    def reset(self):
        self.t = 0
        self.running = False
        self.text(0)

    def update(self):
        if self.running:
            self.text(int(time() - self.t))
            self.label.after(1000, self.update)
