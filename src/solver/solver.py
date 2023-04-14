from copy import deepcopy
from consts.states import States


class Solver:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper

    def solve(self):
        self.init_state()

    def get_state(self, cell):
        return self.state[cell[0]][cell[1]]

    def set_state(self, cell, state):
        self.state[cell[0]][cell[1]] = state

    def init_state(self):
        self.state = deepcopy(self.minesweeper.game.state)
        for x in range(self.minesweeper.gui.width):
            for y in range(self.minesweeper.gui.height):
                if self.get_state((x, y)) < States.COVERED:
                    self.get_state((x, y), States.COVERED)

    def neighbors(self, cell):
        for nx in range(cell[0]-1, cell[0]+2):
            for ny in range(cell[1]-1, cell[1]+2):
                if (nx, ny) != cell and self.minesweeper.gui.inside((nx, ny)):
                    yield nx, ny

    def neighbors_stats(self, cell):
        covered = 0
        uncovered = 0
        mines = 0
        for neighbor in self.neighbors(cell):
            state = self.get_state(neighbor)
            if state == States.COVERED:
                covered += 1
            elif state == States.MINE:
                mines += 1
            else:
                uncovered += 1
        return covered, uncovered, mines

    def set_mines(self, cell):
        for neighbor in self.neighbors(cell):
            if self.get_state(neighbor) == States.COVERED:
                self.set_state(neighbor, States.MINE)
