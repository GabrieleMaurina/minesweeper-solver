import tkinter as tk
from consts.colors import Colors
from consts.consts import Consts


TEXT_SIZE = 20
SIZE = 3


class Display:
    def __init__(self, root):
        self.label = tk.Label(root, font=(None, TEXT_SIZE, 'bold'),
                              bg=Colors.BLACK, fg=Colors.RED, border=Consts.SMALL_BORDER, relief='sunken', width=SIZE)

    def grid(self, *args, **kwargs):
        self.label.grid(*args, **kwargs)

    def text(self, value):
        self.label['text'] = str(value).zfill(SIZE)
