import tkinter.font as tkfont
from operator import add
from colors import Colors
from consts import Consts

COVER_DELTA = 4
EMPTY_DELTA = 1
MINE_DELTA = 7
MINE_WHITE_DELTA = 11
MINE_WIDTH = 3

FONT_SIZE = 15


class Drawer:
    def __init__(self, board):
        self.board = board

    def coords(self, cell):
        x1 = cell[0] * Consts.CELL_SIZE + 2
        x2 = x1 + Consts.CELL_SIZE
        y1 = cell[1] * Consts.CELL_SIZE + 2
        y2 = y1 + Consts.CELL_SIZE
        return x1, x2, y1, y2

    def draw_empty(self, cell):
        x1, x2, y1, y2 = self.coords(cell)
        self.board.canvas.create_rectangle(
            x1, y1, x2, y2, fill=Colors.GRAY, outline='')

    def draw_uncovered(self, cell, red=False):
        x1, x2, y1, y2 = self.coords(cell)
        self.board.canvas.create_rectangle(
            x1, y1, x2, y2, fill=Colors.DARK_GRAY, outline='')
        self.board.canvas.create_rectangle(
            x1 + EMPTY_DELTA, y1 + EMPTY_DELTA, x2 - EMPTY_DELTA, y2 - EMPTY_DELTA, fill=Colors.RED if red else Colors.GRAY, outline='')

    def draw_covered(self, cell):
        x1, x2, y1, y2 = self.coords(cell)
        self.board.canvas.create_rectangle(
            x1, y1, x2, y2, fill=Colors.DARK_GRAY, outline='')
        self.board.canvas.create_polygon(
            (x1, y1, x2, y1, x1, y2), fill=Colors.LIGHT_GRAY, outline='')
        self.board.canvas.create_rectangle(
            x1 + COVER_DELTA, y1 + COVER_DELTA, x2 - COVER_DELTA, y2 - COVER_DELTA, fill=Colors.GRAY, outline='')

    def get_number_color(self, number):
        return Colors.NUMBER_COLORS[number - 1]

    def draw_number(self, number, cell):
        self.draw_uncovered(cell)
        x1, x2, y1, y2 = self.coords(cell)
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        color = self.get_number_color(number)
        font = tkfont.Font(size=FONT_SIZE, weight='bold')
        self.board.canvas.create_text(
            x_center, y_center, text=number, fill=color, font=font)

    def draw_flag(self, cell):
        self.draw_covered(cell)
        x1, x2, y1, y2 = self.coords(cell)
        flag_d1 = 7
        flag_d2 = 12
        flag_d3 = 20
        self.board.canvas.create_rectangle(
            x1 + flag_d1, y1 + flag_d3, x2 - flag_d1, y2 - flag_d1, fill=Colors.BLACK, outline='')
        self.board.canvas.create_rectangle(
            x1 + flag_d2, y1 + flag_d2, x2 - flag_d2, y2 - flag_d1, fill=Colors.BLACK, outline='')
        flag_coords = (18, 5, 18, 17, 6, 12)
        self.board.canvas.create_polygon(
            tuple(map(add, flag_coords, ((x1, y1) * 3))), fill=Colors.RED, outline='')

    def draw_mine(self, cell, red=False):
        self.draw_uncovered(cell, red=red)
        x1, x2, y1, y2 = self.coords(cell)
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        self.board.canvas.create_oval(x1 + MINE_DELTA, y1 + MINE_DELTA,
                                      x2 - MINE_DELTA, y2 - MINE_DELTA, fill=Colors.BLACK, outline='')
        self.board.canvas.create_line(x1 + COVER_DELTA, y_center,
                                      x2 - COVER_DELTA, y_center, fill=Colors.BLACK, width=MINE_WIDTH)
        self.board.canvas.create_line(x_center, y1 + COVER_DELTA,
                                      x_center, y2 - COVER_DELTA, fill=Colors.BLACK, width=MINE_WIDTH)
        self.board.canvas.create_line(x1 + MINE_DELTA, y1 + MINE_DELTA,
                                      x2 - MINE_DELTA, y2 - MINE_DELTA, fill=Colors.BLACK, width=MINE_WIDTH)
        self.board.canvas.create_line(x1 + MINE_DELTA, y2 - MINE_DELTA,
                                      x2 - MINE_DELTA, y1 + MINE_DELTA, fill=Colors.BLACK, width=MINE_WIDTH)
        self.board.canvas.create_oval(x1 + MINE_WHITE_DELTA, y1 + MINE_WHITE_DELTA,
                                      x_center, y_center, fill=Colors.WHITE, outline='')

    def draw_red_mine(self, cell):
        self.draw_mine(cell, red=True)
