from consts import Consts
from colors import Colors


class Segments:
    def __init__(self, canvas, index):
        self.canvas = canvas
        self.index = index
        self.delta = Consts.DISPLAY_WIDTH * self.index

    def update(self, value):
        if value == Consts.DISPLAY_OFF:
            self.canvas.create_rectangle(
                self.delta, 0, self.delta + Consts.DISPLAY_WIDTH, Consts.DISPLAY_HEIGHT, fill=Colors.BLACK)
        elif value == Consts.DISPLAY_ON:
            self.canvas.create_rectangle(
                self.delta, 0, self.delta + Consts.DISPLAY_WIDTH, Consts.DISPLAY_HEIGHT, fill=Colors.DARK_RED)
