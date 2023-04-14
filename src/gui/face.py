import tkinter as tk
from consts.consts import Consts
from consts.states import States


class Face:
    def __init__(self, home):
        self.home = home
        self.button = tk.Button(self.home.menu_frame,
                                borderwidth=Consts.SMALL_BORDER, command=self.click)
        self.set_status(States.SMILE)

    def set_status(self, status):
        self.status = status
        self.button.configure(image=self.home.gui.images.dict[status])

    def click(self):
        self.home.gui.show_home_page()

    def grid(self, *args, **kwargs):
        self.button.grid(*args, **kwargs)
