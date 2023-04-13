import tkinter as tk
from consts.consts import Consts
from gui.display.counter import Counter
from gui.display.timer import Timer


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
        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.columnconfigure(4, weight=1)

        self.counter_display = Counter(self.menu_frame)
        self.counter_display.grid(row=0, column=0, sticky=tk.W)

        self.back_button = tk.Button(
            self.menu_frame, text='Back', command=self.gui.show_settings_page, font=self.gui.font)
        self.back_button.grid(row=0, column=1)

        self.next_button = tk.Button(
            self.menu_frame, text='Next', command=None, font=self.gui.font)
        self.next_button.grid(row=0, column=2)

        self.solve_button = tk.Button(
            self.menu_frame, text='Solve', command=None, font=self.gui.font)
        self.solve_button.grid(row=0, column=3)

        self.timer_display = Timer(self.menu_frame)
        self.timer_display.grid(row=0, column=4, sticky=tk.E)

    def hide(self):
        self.home_frame.pack_forget()

    def show(self):
        self.home_frame.pack(fill=tk.BOTH, expand=True)
        self.counter_display.set(self.gui.minesweeper.game.n_mines)
