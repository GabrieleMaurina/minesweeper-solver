from random import randrange, sample
from functools import partial


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
        self.state = [[randrange(-4, 9) for y in range(self.minesweeper.gui.height())]
                      for x in range(self.minesweeper.gui.width())]

    def coords(self, width, n):
        x = n % width
        y = n // width
        return x, y
