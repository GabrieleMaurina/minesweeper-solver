import platform
import tkinter as tk
import tkinter.font as tkfont
from gui.settings import Settings, DEFAULT_HEIGHT, DEFAULT_WIDTH, DEFAULT_MINES
from gui.home import Home
from consts.images import Images


FONT_SIZE = 10


class GUI:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.fix_res()
        self.root = tk.Tk()
        self.root.title('Minesweeper')
        self.font = tkfont.Font(size=FONT_SIZE, weight='bold')
        self.images = Images()
        self.settings = Settings(self)
        self.home = Home(self)
        self.show_settings_page()

    def start(self):
        self.root.mainloop()

    def fix_res(self):
        os = platform.system()
        if os == 'Windows':
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)

    def show_settings_page(self):
        self.settings.show()
        self.home.hide()

    def show_home_page(self):
        self.minesweeper.game.init_state()
        self.minesweeper.board.resize()
        self.settings.hide()
        self.home.show()

    def width(self):
        try:
            return int(self.settings.width_variable.get())
        except ValueError:
            return DEFAULT_WIDTH

    def height(self):
        try:
            return int(self.settings.height_variable.get())
        except ValueError:
            return DEFAULT_HEIGHT

    def mines(self):
        try:
            return int(self.settings.mines_variable.get())
        except ValueError:
            return DEFAULT_MINES

    def inside(self, cell):
        x, y = cell
        return x >= 0 and y >= 0 and x < self.width() and y < self.height()
