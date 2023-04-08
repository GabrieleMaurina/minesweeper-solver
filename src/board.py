import tkinter as tk
import tkinter.font as tkfont
from operator import add
from game import States


CELL_SIZE = 30
COVER_DELTA = 3
EMPTY_DELTA = 1
MINE_DELTA = 7
MINE_WHITE_DELTA = 11
MINE_WIDTH = 3

FONT_SIZE = 15

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

BLACK = '#000000'
WHITE = '#ffffff'
RED = '#ff0000'


class Board:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.canvas = tk.Canvas(self.minesweeper.gui.main_page_frame, bg=GRAY)
        self.init_mouse()

    def resize(self):
        self.canvas.configure(width=CELL_SIZE * self.minesweeper.gui.width(),
                              height=CELL_SIZE * self.minesweeper.gui.height())
        self.canvas.grid(row=1, column=0, columnspan=4)
        self.draw_board()

    def draw_board(self):
        for x in range(self.minesweeper.gui.width()):
            for y in range(self.minesweeper.gui.height()):
                self.draw_cell(x, y)

    def draw_cell(self, x, y):
        v = self.minesweeper.game.state[x][y]
        if v > 0 and v < 9:
            self.draw_number(x, y, v)
        elif v == States.UNCOVERED:
            self.draw_uncovered(x, y)
        elif v == States.COVERED:
            self.draw_covered(x, y)
        elif v == States.FLAG:
            self.draw_flag(x, y)
        elif v == States.MINE:
            self.draw_mine(x, y)
        elif v == States.RED_MINE:
            self.draw_red_mine(x, y)
        else:
            raise ValueError(f'Invalid value: {v}')

    def coords(self, x, y):
        x1 = x * CELL_SIZE + 2
        x2 = x1 + CELL_SIZE
        y1 = y * CELL_SIZE + 2
        y2 = y1 + CELL_SIZE
        return x1, x2, y1, y2

    def draw_empty(self, x, y):
        x1, x2, y1, y2 = self.coords(x, y)
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=GRAY, outline='')

    def draw_uncovered(self, x, y, red=False):
        x1, x2, y1, y2 = self.coords(x, y)
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=DARK_GRAY, outline='')
        self.canvas.create_rectangle(
            x1 + EMPTY_DELTA, y1 + EMPTY_DELTA, x2 - EMPTY_DELTA, y2 - EMPTY_DELTA, fill=RED if red else GRAY, outline='')

    def draw_covered(self, x, y):
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
        self.draw_uncovered(x, y)
        x1, x2, y1, y2 = self.coords(x, y)
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        color = self.get_number_color(number)
        font = tkfont.Font(size=FONT_SIZE, weight='bold')
        self.canvas.create_text(
            x_center, y_center, text=number, fill=color, font=font)

    def draw_flag(self, x, y):
        self.draw_covered(x, y)
        x1, x2, y1, y2 = self.coords(x, y)
        flag_d1 = 7
        flag_d2 = 12
        flag_d3 = 20
        self.canvas.create_rectangle(
            x1 + flag_d1, y1 + flag_d3, x2 - flag_d1, y2 - flag_d1, fill=BLACK, outline='')
        self.canvas.create_rectangle(
            x1 + flag_d2, y1 + flag_d2, x2 - flag_d2, y2 - flag_d1, fill=BLACK, outline='')
        flag_coords = (18, 5, 18, 17, 6, 12)
        self.canvas.create_polygon(
            tuple(map(add, flag_coords, ((x1, y1) * 3))), fill=RED, outline='')

    def draw_mine(self, x, y, red=False):
        self.draw_uncovered(x, y, red=red)
        x1, x2, y1, y2 = self.coords(x, y)
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        self.canvas.create_oval(x1 + MINE_DELTA, y1 + MINE_DELTA,
                                x2 - MINE_DELTA, y2 - MINE_DELTA, fill=BLACK, outline='')
        self.canvas.create_line(x1 + COVER_DELTA, y_center,
                                x2 - COVER_DELTA, y_center, fill=BLACK, width=MINE_WIDTH)
        self.canvas.create_line(x_center, y1 + COVER_DELTA,
                                x_center, y2 - COVER_DELTA, fill=BLACK, width=MINE_WIDTH)
        self.canvas.create_line(x1 + MINE_DELTA, y1 + MINE_DELTA,
                                x2 - MINE_DELTA, y2 - MINE_DELTA, fill=BLACK, width=MINE_WIDTH)
        self.canvas.create_line(x1 + MINE_DELTA, y2 - MINE_DELTA,
                                x2 - MINE_DELTA, y1 + MINE_DELTA, fill=BLACK, width=MINE_WIDTH)
        self.canvas.create_oval(x1 + MINE_WHITE_DELTA, y1 + MINE_WHITE_DELTA,
                                x_center, y_center, fill=WHITE, outline='')

    def draw_red_mine(self, x, y):
        self.draw_mine(x, y, True)

    def get_cell(self, x, y):
        x = int(x / CELL_SIZE)
        y = int(y / CELL_SIZE)
        return x, y

    def init_mouse(self):
        self.mouse_down = False
        self.last_cell = None
        self.canvas.bind('<ButtonPress-1>', self.on_mouse_down)
        self.canvas.bind('<ButtonRelease-1>', self.on_mouse_up)
        self.canvas.bind('<Motion>', self.on_mouse_motion)
        self.canvas.bind('<Button-3>', self.on_right_click)

    def on_mouse_down(self, event):
        self.mouse_down = True
        self.on_down(event)

    def on_mouse_up(self, _):
        self.mouse_down = False
        if self.last_cell:
            x = self.last_cell[0]
            y = self.last_cell[1]
            self.last_cell = None
            state = self.minesweeper.game.state[x][y]
            if state == States.COVERED or state == States.FLAG:
                self.minesweeper.game.click(x, y)

    def on_mouse_motion(self, event):
        if self.mouse_down:
            self.on_down(event)

    def on_down(self, event):
        x, y = self.get_cell(event.x, event.y)
        if (x, y) != self.last_cell:
            if self.last_cell:
                self.draw_cell(self.last_cell[0], self.last_cell[1])
            if x > 0 and y > 0 and x < self.minesweeper.gui.width() and y < self.minesweeper.gui.height():
                self.last_cell = x, y
                state = self.minesweeper.game.state[x][y]
                if state == States.COVERED or state == States.FLAG:
                    self.draw_empty(x, y)
            else:
                self.last_cell = None

    def on_right_click(self, event):
        x, y = self.get_cell(event.x, event.y)
        if x > 0 and y > 0 and x < self.minesweeper.gui.width() and y < self.minesweeper.gui.height():
            self.minesweeper.game.right_click(x, y)
