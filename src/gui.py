import platform
import tkinter as tk
import tkinter.font as tkfont


DEFAULT_WIDTH = 20
DEFAULT_HEIGHT = 20
DEFAULT_MINES = 20

FONT_SIZE = 10


class GUI:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.fix_res()
        self.root = tk.Tk()
        self.root.title('Minesweeper')
        self.font = tkfont.Font(size=FONT_SIZE, weight='bold')
        self.create_settings_page()
        self.create_main_page()
        self.show_settings_page()

    def start(self):
        self.root.mainloop()

    def fix_res(self):
        os = platform.system()
        if os == 'Windows':
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)

    def create_settings_page(self):
        self.settings_page_frame = tk.Frame(self.root)
        self.integer_only = (
            (self.root.register(lambda v: str.isdigit(v))), '%P')
        self.width_label = tk.Label(
            self.settings_page_frame, text='Width', font=self.font)
        self.width_label.grid(row=0, column=0)
        self.width_variable = tk.StringVar(self.root, DEFAULT_WIDTH)
        self.width_entry = tk.Entry(
            self.settings_page_frame, width=4, textvariable=self.width_variable, validate='all', validatecommand=self.integer_only, font=self.font)
        self.width_entry.grid(row=0, column=1)
        self.height_label = tk.Label(
            self.settings_page_frame, text='Height', font=self.font)
        self.height_label.grid(row=1, column=0)
        self.height_variable = tk.StringVar(self.root, DEFAULT_HEIGHT)
        self.height_entry = tk.Entry(
            self.settings_page_frame, width=4, textvariable=self.height_variable, validate='all', validatecommand=self.integer_only, font=self.font)
        self.height_entry.grid(row=1, column=1)
        self.mines_label = tk.Label(
            self.settings_page_frame, text='Mines', font=self.font)
        self.mines_label.grid(row=2, column=0)
        self.mines_variable = tk.StringVar(self.root, DEFAULT_MINES)
        self.mines_entry = tk.Entry(
            self.settings_page_frame, width=4, textvariable=self.mines_variable, validate='all', validatecommand=self.integer_only, font=self.font)
        self.mines_entry.grid(row=2, column=1)
        self.start_button = tk.Button(
            self.settings_page_frame, text='Start', command=self.show_main_page, font=self.font)
        self.start_button.grid(row=3, column=0, columnspan=2)

    def create_main_page(self):
        self.main_page_frame = tk.Frame(self.root)
        self.main_page_frame.grid_columnconfigure(0, weight=0)
        self.main_page_frame.grid_columnconfigure(1, weight=0)
        self.main_page_frame.grid_columnconfigure(2, weight=0)
        self.main_page_frame.grid_columnconfigure(3, weight=1)
        self.back_button = tk.Button(
            self.main_page_frame, text='Back', command=self.show_settings_page, font=self.font)
        self.back_button.grid(row=0, column=0)
        self.next_button = tk.Button(
            self.main_page_frame, text='Next', command=None, font=self.font)
        self.next_button.grid(row=0, column=1)
        self.solve_button = tk.Button(
            self.main_page_frame, text='Solve', command=None, font=self.font)
        self.solve_button.grid(row=0, column=2)

    def show_settings_page(self):
        self.settings_page_frame.pack()
        self.main_page_frame.pack_forget()

    def show_main_page(self):
        self.minesweeper.game.init_state()
        self.minesweeper.board.resize()
        self.main_page_frame.pack()
        self.settings_page_frame.pack_forget()

    def width(self):
        try:
            return int(self.width_variable.get())
        except ValueError:
            return DEFAULT_WIDTH

    def height(self):
        try:
            return int(self.height_variable.get())
        except ValueError:
            return DEFAULT_HEIGHT

    def mines(self):
        try:
            return int(self.mines_variable.get())
        except ValueError:
            return DEFAULT_MINES

    def inside(self, cell):
        x, y = cell
        return x >= 0 and y >= 0 and x < self.width() and y < self.height()
