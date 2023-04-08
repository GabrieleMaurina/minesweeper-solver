from gui import GUI
from board import Board
from game import Game


class Minesweeper:
    def __init__(self):
        self.gui = GUI(self)
        self.board = Board(self)
        self.game = Game(self)
        self.gui.start()


def main():
    Minesweeper()


if __name__ == '__main__':
    main()
