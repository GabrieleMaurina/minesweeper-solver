import tkinter as tk
import tkinter.font as tkfont
from random import randrange


CELL_SIZE = 20
COVER_DELTA = 2
EMPTY_DELTA = 1
FONT_DELTA = 6

GRAY = '#c0c0c0'
DARK_GRAY = '#777777'
LIGHT_GRAY = '#eeeeee'

ONE_COLOR = '#0000ff'
TWO_COLOR = '#007b00'
THREE_COLOR = '#ff0000'
FOUR_COLOR = '#00007b'
FIVE_COLOR = '#7b0000'
SIX_COLOR = '#007b7b'
SEVEN_COLOR = '#7b007b'
EIGHT_COLOR = '#7b7b7b'

NUMBER_COLORS = (ONE_COLOR, TWO_COLOR, THREE_COLOR, FOUR_COLOR,
                 FIVE_COLOR, SIX_COLOR, SEVEN_COLOR, EIGHT_COLOR)


class Board:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.canvas = tk.Canvas(self.minesweeper.main_page_frame, bg=GRAY)

    def resize(self):
        self.canvas.configure(width=CELL_SIZE * self.minesweeper.width(),
                              height=CELL_SIZE * self.minesweeper.height())
        self.canvas.grid(row=1, column=0, columnspan=4)
        for x in range(self.minesweeper.width()):
            for y in range(self.minesweeper.height()):
                self.draw_cover(x, y)
                # self.draw_number(x, y, randrange(8) + 1)

    def coords(self, x, y):
        x1 = x * CELL_SIZE + 2
        x2 = x1 + CELL_SIZE
        y1 = y * CELL_SIZE + 2
        y2 = y1 + CELL_SIZE
        return x1, x2, y1, y2

    def draw_empty(self, x, y):
        x1, x2, y1, y2 = self.coords(x, y)
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=DARK_GRAY, outline='')
        x_delta = EMPTY_DELTA if x == self.minesweeper.width() - 1 else 0
        y_delta = EMPTY_DELTA if y == self.minesweeper.height() - 1 else 0
        self.canvas.create_rectangle(
            x1 + EMPTY_DELTA, y1 + EMPTY_DELTA, x2 - x_delta, y2 - y_delta, fill=GRAY, outline='')

    def draw_cover(self, x, y):
        x1, x2, y1, y2 = self.coords(x, y)
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=DARK_GRAY, outline='')
        self.canvas.create_polygon(
            (x1, y1, x2, y1, x1, y2), fill=LIGHT_GRAY, outline='')
        self.canvas.create_rectangle(
            x1 + COVER_DELTA, y1 + COVER_DELTA, x2 - COVER_DELTA, y2 - COVER_DELTA, fill=GRAY, outline='')

    def get_number_color(self, number):
        return NUMBER_COLORS[number - 1]

    def draw_number(self, x, y, number):
        self.draw_empty(x, y)
        x1, x2, y1, y2 = self.coords(x, y)
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2 + 1
        color = self.get_number_color(number)
        font = tkfont.Font(size=CELL_SIZE-FONT_DELTA, weight='bold')
        self.canvas.create_text(
            x_center, y_center, text=number, fill=color, font=font)
