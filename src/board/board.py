import tkinter as tk
from misc.game import States
from consts.consts import Consts
from consts.colors import Colors


class Board:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.canvas_frame = tk.Frame(
            self.minesweeper.gui.home.home_frame, borderwidth=Consts.BORDER, relief='sunken')
        self.canvas = tk.Canvas(self.canvas_frame, bg=Colors.GRAY)
        self.canvas_cells = {}
        self.canvas.pack()

    def resize(self):
        for image in self.canvas_cells.values():
            self.canvas.delete(image)
        self.canvas.configure(width=Consts.CELL_SIZE * self.minesweeper.gui.width(),
                              height=Consts.CELL_SIZE * self.minesweeper.gui.height())
        self.canvas_frame.pack(padx=Consts.PAD, pady=Consts.PAD, expand=True)
        self.update_board()

    def update_cell(self, cell):
        self.empty_cell(cell)
        status = self.minesweeper.game.get_state(cell)
        new_image = self.minesweeper.gui.images.dict[status]
        self.canvas_cells[cell] = self.canvas.create_image(
            cell[0] * Consts.CELL_SIZE, cell[1] * Consts.CELL_SIZE, image=new_image, anchor='nw')

    def empty_cell(self, cell):
        if cell in self.canvas_cells:
            self.canvas.delete(self.canvas_cells[cell])

    def update_board(self):
        for x in range(self.minesweeper.gui.width()):
            for y in range(self.minesweeper.gui.height()):
                self.update_cell((x, y))

    def get_cell(self, cell):
        x = int(cell[0] / Consts.CELL_SIZE)
        y = int(cell[1] / Consts.CELL_SIZE)
        return x, y
