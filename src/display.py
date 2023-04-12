import tkinter as tk
from colors import Colors
from consts import Consts


class Display:
    def __init__(self, root):
        self.label = tk.Label(root, text='000', font=(None, 20),
                              bg=Colors.BLACK, fg=Colors.RED, border=Consts.SMALL_BORDER, relief='sunken')

    def grid(self, *args, **kwargs):
        self.label.grid(*args, **kwargs)

    def text(self, value):
        self.label['text'] = value
