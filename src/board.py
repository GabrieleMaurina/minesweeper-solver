import tkinter as tk
from game import States
from colors import Colors
from drawer import Drawer, CELL_SIZE


class Board:

    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.canvas = tk.Canvas(
            self.minesweeper.gui.main_page_frame, bg=Colors.GRAY)
        self.drawer = Drawer(self)

    def resize(self):
        self.canvas.configure(width=CELL_SIZE * self.minesweeper.gui.width(),
                              height=CELL_SIZE * self.minesweeper.gui.height())
        self.canvas.grid(row=1, column=0, columnspan=4)
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
        x = int(cell[0] / CELL_SIZE)
        y = int(cell[1] / CELL_SIZE)
        return x, y
