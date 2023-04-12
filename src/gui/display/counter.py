from gui.display.display import Display


class Counter(Display):
    def __init__(self, root):
        super().__init__(root)
        self.set(0)

    def set(self, value):
        self.value = value
        self.text(self.value)

    def inc(self):
        self.value += 1
        self.text(self.value)

    def dec(self):
        self.value -= 1
        self.text(self.value)
