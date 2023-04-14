import tkinter as tk
from consts.consts import Consts
from consts.states import States
from gui.display.counter import Counter
from gui.display.timer import Timer
from gui.face import Face


class Home:
    def __init__(self, gui):
        self.gui = gui
        self.create_components()

    def create_components(self):

        self.home_frame = tk.Frame(
            self.gui.root, borderwidth=Consts.BORDER, relief='raised')

        self.menu_frame = tk.Frame(
            self.home_frame, borderwidth=Consts.BORDER, relief='sunken')
        self.menu_frame.pack(fill=tk.X, padx=Consts.PAD, pady=(Consts.PAD, 0))
        for i in range(5):
            self.menu_frame.columnconfigure(i, weight=1)

        self.counter_display = Counter(self.menu_frame)
        self.counter_display.grid(row=0, column=0, sticky=tk.W)

        self.back_button = tk.Button(
            self.menu_frame, text='Back', command=self.gui.show_settings_page, font=self.gui.font, borderwidth=Consts.SMALL_BORDER)
        self.back_button.grid(row=0, column=1)

        self.face_button = Face(self)
        self.face_button.grid(row=0, column=2)

        self.solve_button = tk.Button(
            self.menu_frame, text='Solve', command=None, font=self.gui.font, borderwidth=Consts.SMALL_BORDER)
        self.solve_button.grid(row=0, column=3)

        self.timer_display = Timer(self.menu_frame)
        self.timer_display.grid(row=0, column=4, sticky=tk.E)

    def hide(self):
        self.home_frame.pack_forget()

    def show(self):
        self.home_frame.pack(fill=tk.BOTH, expand=True)
        self.counter_display.set(self.gui.minesweeper.game.n_mines)
        self.face_button.set_status(States.SMILE)
