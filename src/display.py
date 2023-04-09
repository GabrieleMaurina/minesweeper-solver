import tkinter as tk
from segments import Segments
from colors import Colors
from consts import Consts


class Display:
    def __init__(self, root, digits):
        self.root = root
        self.digits = digits
        self.canvas = tk.Canvas(
            root, width=Consts.DISPLAY_WIDTH * digits, height=Consts.DISPLAY_HEIGHT, bg=Colors.BLACK)
        self.segments = [Segments(self.canvas, i)
                         for i in reversed(range(digits))]

    def pack(self, *args, **kwargs):
        self.canvas.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self.canvas.grid(*args, **kwargs)

    def on(self):
        for segment in self.segments:
            segment.update(Consts.DISPLAY_ON)

    def off(self):
        for segment in self.segments:
            segment.update(Consts.DISPLAY_OFF)

    def set_value(self, value):
        if value < 0:
            return
        for pos, segment in enumerate(self.segments):
            segment.update(self.get_digit(value, pos))

    def get_digit(self, value, digit):
        return value // (10**digit) % 10
