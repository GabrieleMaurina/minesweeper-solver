import tkinter as tk
from game import States
from drawer import Drawer
from consts import Consts


class Board:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.canvas_frame = tk.Frame(
            self.minesweeper.gui.home.home_frame, borderwidth=Consts.BORDER, relief='sunken')
        self.canvas = tk.Canvas(self.canvas_frame)
        self.canvas.pack()
        self.drawer = Drawer(self)

    def resize(self):
        self.canvas.configure(width=Consts.CELL_SIZE * self.minesweeper.gui.width(),
                              height=Consts.CELL_SIZE * self.minesweeper.gui.height())
        self.canvas_frame.pack(padx=Consts.PAD, pady=Consts.PAD, expand=True)
        self.draw_board()

    def draw_board(self):
        for x in range(self.minesweeper.gui.width()):
            for y in range(self.minesweeper.gui.height()):
                self.draw_cell((x, y))

    def draw_cell(self, cell):
        v = self.minesweeper.game.get_state(cell)
        if v > 0 and v < 9:
            self.drawer.draw_number(v, cell)
        elif v == States.UNCOVERED:
            self.drawer.draw_uncovered(cell)
        elif v == States.COVERED:
            self.drawer.draw_covered(cell)
        elif v == States.FLAG:
            self.drawer.draw_flag(cell)
        elif v == States.MINE:
            self.drawer.draw_mine(cell)
        elif v == States.RED_MINE:
            self.drawer.draw_red_mine(cell)
        else:
            raise ValueError(f'Cell {cell} invalid state {v}')

    def get_cell(self, cell):
        x = int(cell[0] / Consts.CELL_SIZE)
        y = int(cell[1] / Consts.CELL_SIZE)
        return x, y
