from random import randrange, sample
from functools import partial


class States:
    UNCOVERED = 0
    COVERED = -1
    FLAG = -2
    MINE = -3
    RED_MINE = -4


class Game:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper

    def init_state(self):
        width = self.minesweeper.gui.width()
        height = self.minesweeper.gui.height()
        self.n_cells = width * height
        self.n_mines = min(self.n_cells//4, self.minesweeper.gui.mines())
        mines_sample = sample(range(self.n_cells), self.n_mines)
        self.mines = set(map(partial(self.coords, width), mines_sample))
        # self.state = [[randrange(-4, 9) for y in range(height)]
        #              for x in range(width)]
        self.state = [[-1 for y in range(height)]
                      for x in range(width)]

    def coords(self, width, n):
        x = n % width
        y = n // width
        return x, y

    def click(self, x, y):
        pass

    def right_click(self, x, y):
        if self.state[x][y] == States.COVERED:
            self.state[x][y] = States.FLAG
        elif self.state[x][y] == States.FLAG:
            self.state[x][y] = States.COVERED
        self.minesweeper.board.draw_cell(x, y)
