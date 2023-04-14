from gui.gui import GUI
from board.board import Board
from misc.mouse import Mouse
from misc.game import Game
from solver.solver import Solver
from consts.images import Images


class Minesweeper:
    def __init__(self):
        self.gui = GUI(self)
        self.board = Board(self)
        self.mouse = Mouse(self)
        self.game = Game(self)
        self.solver = Solver(self)
        self.gui.start()


def main():
    Minesweeper()


if __name__ == '__main__':
    main()
