from random import choice
from copy import deepcopy
from consts.states import States


class Solver:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper

    def solve(self):
        for cell in self.clicks():
            self.minesweeper.game.click(cell)
            self.minesweeper.gui.update()

    def get_state(self, cell):
        return self.state[cell[0]][cell[1]]

    def set_state(self, cell, state):
        self.state[cell[0]][cell[1]] = state

    def cells(self):
        for x in range(self.minesweeper.gui.width()):
            for y in range(self.minesweeper.gui.height()):
                yield x, y

    def init_state(self):
        self.state = deepcopy(self.minesweeper.game.state)
        for cell in self.cells():
            if self.get_state(cell) < States.COVERED:
                self.get_state(cell, States.COVERED)

    def update_state(self):
        for cell in self.cells():
            actual_state = self.minesweeper.game.get_state(cell)
            if actual_state > States.COVERED and actual_state != self.get_state(cell):
                self.set_state(cell, actual_state)

    def numbered_cells(self):
        for cell in self.cells():
            state = self.get_state(cell)
            if state > 0:
                covered, mines = self.neighbors_stats(cell)
                yield cell, state, covered, mines

    def clicks(self):
        if self.minesweeper.game.over:
            return
        self.init_state()
        while not self.minesweeper.game.over:
            self.update_state()
            self.find_mines()
            found = False
            for cell, state, covered, mines in self.numbered_cells():
                if covered and state == mines:
                    for neighbor in self.neighbors(cell):
                        if self.clickable(neighbor):
                            yield neighbor
                            found = True
            if not found:
                cell = self.random_clickable()
                yield cell

    def clickable(self, cell):
        return self.get_state(cell) == States.COVERED and self.minesweeper.game.get_state(cell) in States.CLICKABLE

    def random_clickable(self):
        return choice([cell for cell in self.cells() if self.clickable(cell)])

    def find_mines(self):
        changed = True
        while changed:
            changed = False
            for cell, state, covered, mines in self.numbered_cells():
                if covered and state - mines == covered:
                    self.set_mines(cell)
                    changed = True

    def neighbors(self, cell):
        for nx in range(cell[0]-1, cell[0]+2):
            for ny in range(cell[1]-1, cell[1]+2):
                if (nx, ny) != cell and self.minesweeper.gui.inside((nx, ny)):
                    yield nx, ny

    def neighbors_stats(self, cell):
        covered = 0
        mines = 0
        for neighbor in self.neighbors(cell):
            state = self.get_state(neighbor)
            if state == States.COVERED:
                covered += 1
            elif state == States.MINE:
                mines += 1
        return covered, mines

    def set_mines(self, cell):
        for neighbor in self.neighbors(cell):
            if self.get_state(neighbor) == States.COVERED:
                self.set_state(neighbor, States.MINE)
