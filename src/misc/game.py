from random import sample
from functools import partial
from collections import deque
from consts.states import States


class Game:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper

    def init_state(self):
        self.over = False
        self.started = False
        self.minesweeper.gui.home.timer_display.reset()
        width = self.minesweeper.gui.width()
        height = self.minesweeper.gui.height()
        self.n_cells = width * height
        self.n_mines = min(self.n_cells, self.minesweeper.gui.mines())
        mines_sample = sample(range(self.n_cells), self.n_mines)
        self.mines = set(map(partial(self.coords, width), mines_sample))
        self.state = [[States.COVERED for _ in range(height)]
                      for _ in range(width)]

    def coords(self, width, n):
        x = n % width
        y = n // width
        return x, y

    def click(self, cell):
        self.start_timer()
        if cell in self.mines:
            self.game_over(cell)
        self.open(cell)
        self.check_win()

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
                self.set_state(0, cell)
                for neighbor in self.neighbors(cell):
                    queue.append(neighbor)

    def neighboring_mines(self, cell):
        return sum(1 for nx, ny in self.neighbors(cell) if (nx, ny) in self.mines)

    def neighbors(self, cell):
        for nx in range(cell[0]-1, cell[0]+2):
            for ny in range(cell[1]-1, cell[1]+2):
                if (nx, ny) != cell and self.minesweeper.gui.inside((nx, ny)):
                    yield nx, ny

    def right_click(self, cell):
        self.start_timer()
        if self.get_state(cell) == States.COVERED:
            self.set_state(States.FLAG, cell)
        elif self.get_state(cell) == States.FLAG:
            self.set_state(States.QUESTION_MARK, cell)
        elif self.get_state(cell) == States.QUESTION_MARK:
            self.set_state(States.COVERED, cell)

    def start_timer(self):
        if not self.started:
            self.started = True
            self.minesweeper.gui.home.timer_display.start()

    def game_over(self, cell):
        self.over = True
        self.minesweeper.gui.home.timer_display.stop()
        self.set_state(States.RED_MINE, cell)
        for mine in self.mines:
            if mine != cell and self.get_state(mine) != States.FLAG:
                self.set_state(States.MINE, mine)
        self.minesweeper.gui.home.face_button.set_status(States.DEAD)

    def remaining(self, state):
        return state == States.COVERED or state == States.FLAG or state == States.QUESTION_MARK

    def check_win(self):
        if self.over:
            return
        tot = sum(1 for row in self.state for state in row if self.remaining(state))
        if tot == self.n_mines:
            self.over = True
            self.minesweeper.gui.home.timer_display.stop()
            for mine in self.mines:
                if self.get_state(mine) == States.COVERED or self.get_state(mine) == States.QUESTION_MARK:
                    self.set_state(States.FLAG, mine)
            self.minesweeper.gui.home.face_button.set_status(States.SUNGLASSES)

    def get_state(self, cell):
        return self.state[cell[0]][cell[1]]

    def set_state(self, value, cell):
        if self.get_state(cell) != value:
            if value == States.FLAG:
                self.minesweeper.gui.home.counter_display.dec()
            elif self.get_state(cell) == States.FLAG:
                self.minesweeper.gui.home.counter_display.inc()
        self.state[cell[0]][cell[1]] = value
        self.minesweeper.board.update_cell(cell)
