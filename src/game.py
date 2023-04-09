from random import sample
from functools import partial
from collections import deque
from states import States


class Game:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper

    def init_state(self):
        self.over = False
        width = self.minesweeper.gui.width()
        height = self.minesweeper.gui.height()
        self.n_cells = width * height
        self.n_mines = min(self.n_cells//4, self.minesweeper.gui.mines())
        mines_sample = sample(range(self.n_cells), self.n_mines)
        self.mines = set(map(partial(self.coords, width), mines_sample))
        self.state = [[States.COVERED for _ in range(height)]
                      for _ in range(width)]

    def coords(self, width, n):
        x = n % width
        y = n // width
        return x, y

    def click(self, cell):
        if cell in self.mines:
            self.game_over(cell)
        self.open(cell)

    def open(self, cell):
        queue = deque()
        queue.append(cell)
        while queue:
            cell = queue.pop()
            if self.get_state(cell) != States.COVERED and self.get_state(cell) != States.FLAG:
                continue
            mines = self.neighboring_mines(cell)
            if mines:
                self.set_state(mines, cell)
            else:
                self.set_state(States.UNCOVERED, cell)
                for neighbor in self.neighbors(cell):
                    queue.append(neighbor)

    def neighboring_mines(self, cell):
        return sum(1 for nx, ny in self.neighbors(cell) if (nx, ny) in self.mines)

    def neighbors(self, cell):
        width = self.minesweeper.gui.width()
        height = self.minesweeper.gui.height()
        for nx in range(cell[0]-1, cell[0]+2):
            for ny in range(cell[1]-1, cell[1]+2):
                if nx >= 0 and ny >= 0 and nx < width and ny < height and (nx, ny) != (cell[0], cell[1]):
                    yield nx, ny

    def right_click(self, cell):
        if self.get_state(cell) == States.COVERED:
            self.set_state(States.FLAG, cell)
        elif self.get_state(cell) == States.FLAG:
            self.set_state(States.COVERED, cell)

    def game_over(self, cell):
        self.over = True
        self.set_state(States.RED_MINE, cell)
        for mine in self.mines:
            if mine != cell:
                self.set_state(States.MINE, mine)

    def get_state(self, cell):
        return self.state[cell[0]][cell[1]]

    def set_state(self, value, cell):
        self.state[cell[0]][cell[1]] = value
        self.minesweeper.board.draw_cell(cell)
