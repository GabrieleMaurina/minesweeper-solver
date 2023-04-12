from consts.states import States


class Mouse:
    def __init__(self, minesweeper):
        self.minesweeper = minesweeper
        self.mouse_down = False
        self.last_cell = None
        self.minesweeper.board.canvas.bind(
            '<ButtonPress-1>', self.on_mouse_down)
        self.minesweeper.board.canvas.bind(
            '<ButtonRelease-1>', self.on_mouse_up)
        self.minesweeper.board.canvas.bind(
            '<Motion>', self.on_mouse_motion)
        self.minesweeper.board.canvas.bind(
            '<Button-3>', self.on_right_click)

    def on_mouse_down(self, event):
        self.mouse_down = True
        self.on_down(event)

    def on_mouse_up(self, _):
        self.mouse_down = False
        if self.last_cell:
            state = self.minesweeper.game.get_state(self.last_cell)
            if state == States.COVERED or state == States.FLAG:
                if self.minesweeper.game.over:
                    self.minesweeper.board.draw_cell(self.last_cell)
                else:
                    self.minesweeper.game.click(self.last_cell)
            self.last_cell = None

    def on_mouse_motion(self, event):
        if self.mouse_down:
            self.on_down(event)

    def on_down(self, event):
        cell = self.minesweeper.board.get_cell((event.x, event.y))
        if cell != self.last_cell:
            if self.last_cell:
                self.minesweeper.board.draw_cell(self.last_cell)
            if self.minesweeper.gui.inside(cell):
                self.last_cell = cell
                state = self.minesweeper.game.get_state(cell)
                if state == States.COVERED or state == States.FLAG:
                    self.minesweeper.board.drawer.draw_empty(cell)
            else:
                self.last_cell = None

    def on_right_click(self, event):
        if self.minesweeper.game.over:
            return
        cell = self.minesweeper.board.get_cell((event.x, event.y))
        if self.minesweeper.gui.inside(cell):
            self.minesweeper.game.right_click(cell)
