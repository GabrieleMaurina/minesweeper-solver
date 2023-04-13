import tkinter as tk
from misc.game import States
from board.drawer import Drawer
from consts.consts import Consts
from consts.colors import Colors
from board.cell import Cell


class Board:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.canvas_frame = tk.Frame(
            self.minesweeper.gui.home.home_frame, borderwidth=Consts.BORDER, relief='sunken')
        self.canvas = tk.Canvas(self.canvas_frame, bg=Colors.GRAY)
        self.canvas.pack()
        self.drawer = Drawer(self)
        self.cells = [[Cell(self, (x, y)) for y in range(
            self.minesweeper.gui.height())] for x in range(self.minesweeper.gui.width())]

    def resize(self):
        self.canvas.configure(width=Consts.CELL_SIZE * self.minesweeper.gui.width(),
                              height=Consts.CELL_SIZE * self.minesweeper.gui.height())
        self.canvas_frame.pack(padx=Consts.PAD, pady=Consts.PAD, expand=True)
        self.draw_board()

    def draw_board(self):
        for column in self.cells:
            for cell in column:
                cell.update()

    def draw_cell(self, cell):
        self.cells[cell[0]][cell[1]].update()

    def get_cell(self, cell):
        x = int(cell[0] / Consts.CELL_SIZE)
        y = int(cell[1] / Consts.CELL_SIZE)
        return x, y
