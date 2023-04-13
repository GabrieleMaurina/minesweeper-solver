from consts.states import States


class Cell:
    def __init__(self, board, cell):
        self.board = board
        self.cell = cell

    def update(self):
        v = self.board.minesweeper.game.get_state(self.cell)
        if v > 0 and v < 9:
            self.board.drawer.draw_number(v, self.cell)
        elif v == States.UNCOVERED:
            self.board.drawer.draw_uncovered(self.cell)
        elif v == States.COVERED:
            self.board.drawer.draw_covered(self.cell)
        elif v == States.FLAG:
            self.board.drawer.draw_flag(self.cell)
        elif v == States.MINE:
            self.board.drawer.draw_mine(self.cell)
        elif v == States.RED_MINE:
            self.board.drawer.draw_red_mine(self.cell)
        else:
            raise ValueError(f'Cell {self.cell} invalid state {v}')
