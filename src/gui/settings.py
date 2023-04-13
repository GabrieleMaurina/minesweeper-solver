import tkinter as tk
from consts.consts import Consts
from consts.colors import Colors


DEFAULT_WIDTH = 20
DEFAULT_HEIGHT = 20
DEFAULT_MINES = 40


class Settings:
    def __init__(self, gui):
        self.gui = gui
        self.create_components()

    def create_components(self):
        self.settings_page_frame = tk.Frame(
            self.gui.root, borderwidth=Consts.BORDER, relief='raised')

        self.settings_frame = tk.Frame(
            self.settings_page_frame, borderwidth=Consts.BORDER, relief='sunken')
        self.settings_frame.pack(expand=True, padx=Consts.PAD, pady=Consts.PAD)
        self.integer_only = (
            (self.gui.root.register(lambda v: str.isdigit(v))), '%P')

        self.width_label = tk.Label(
            self.settings_frame, text='Width', font=self.gui.font)
        self.width_label.grid(row=0, column=0)
        self.width_variable = tk.StringVar(self.gui.root, DEFAULT_WIDTH)
        self.width_entry = tk.Entry(
            self.settings_frame, width=3, textvariable=self.width_variable, validate='all',
            validatecommand=self.integer_only, font=self.gui.font, fg=Colors.DARK_DARK_GRAY)
        self.width_entry.grid(row=0, column=1)

        self.height_label = tk.Label(
            self.settings_frame, text='Height', font=self.gui.font)
        self.height_label.grid(row=1, column=0)
        self.height_variable = tk.StringVar(self.gui.root, DEFAULT_HEIGHT)
        self.height_entry = tk.Entry(
            self.settings_frame, width=3, textvariable=self.height_variable, validate='all',
            validatecommand=self.integer_only, font=self.gui.font, fg=Colors.DARK_DARK_GRAY)
        self.height_entry.grid(row=1, column=1)

        self.mines_label = tk.Label(
            self.settings_frame, text='Mines', font=self.gui.font)
        self.mines_label.grid(row=2, column=0)
        self.mines_variable = tk.StringVar(self.gui.root, DEFAULT_MINES)
        self.mines_entry = tk.Entry(
            self.settings_frame, width=3, textvariable=self.mines_variable, validate='all',
            validatecommand=self.integer_only, font=self.gui.font, fg=Colors.DARK_DARK_GRAY)
        self.mines_entry.grid(row=2, column=1)

        self.start_button = tk.Button(
            self.settings_frame, text='Start', command=self.gui.show_main_page,
            font=self.gui.font, borderwidth=Consts.SMALL_BORDER,)
        self.start_button.grid(row=3, column=0, columnspan=2)

    def hide(self):
        self.settings_page_frame.pack_forget()

    def show(self):
        self.settings_page_frame.pack(fill=tk.BOTH, expand=True)
