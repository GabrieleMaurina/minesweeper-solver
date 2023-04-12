from gui.gui import GUI
from board.board import Board
from mouse import Mouse
from game import Game
from solver import Solver


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
