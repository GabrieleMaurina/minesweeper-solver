from random import randrange


class Game:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.init_state()

    def init_state(self):
        self.state = [[randrange(-4, 9) for y in range(self.minesweeper.gui.height())]
                      for x in range(self.minesweeper.gui.width())]
