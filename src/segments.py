from consts import Consts
from colors import Colors


SEGMENTS = ((0, 2, 3, 5, 6, 7, 8, 9),
            (0, 1, 3, 4, 7, 8, 9),
            (0, 1, 3, 4, 5, 6, 7, 8, 9),
            (0, 2, 3, 5, 6, 8, 9),
            (0, 2, 6, 8),
            (0, 4, 5, 6, 8, 9),
            (0, 2, 3, 4, 5, 6, 8, 9))


class Segments:
    def __init__(self, canvas, index):
        self.canvas = canvas
        self.index = index
        self.coords = (Consts.DISPLAY_WIDTH * self.index,
                       Consts.DISPLAY_WIDTH * (self.index + 1))
        self.segments = (self.zero, self.one, self.two,
                         self.three, self.four, self.five, self.six)

    def update(self, value):
        if value == Consts.DISPLAY_OFF:
            self.canvas.create_rectangle(
                self.delta, 0, self.delta + Consts.DISPLAY_WIDTH, Consts.DISPLAY_HEIGHT, fill=Colors.BLACK)
        elif value == Consts.DISPLAY_ON:
            for draw in self.segments:
                draw(Colors.DARK_RED)
        elif value > -1 and value < 10:
            for segment, draw in zip(SEGMENTS, self.segments):
                if value in segment:
                    draw()
                else:
                    draw(Colors.DARK_RED)
        else:
            raise ValueError(f'Invalid segment display value: {value}')

    def zero(self, color=Colors.RED):
        points = (self.coords[0] + Consts.SEGMENT_DELTA,
                  Consts.SEGMENT_DELTA,
                  self.coords[1] - Consts.SEGMENT_DELTA,
                  Consts.SEGMENT_DELTA,
                  self.coords[1] - Consts.SEGMENT_DELTA - Consts.SEGMENT_WIDTH,
                  Consts.SEGMENT_DELTA + Consts.SEGMENT_WIDTH,
                  self.coords[0] + Consts.SEGMENT_DELTA + Consts.SEGMENT_WIDTH,
                  Consts.SEGMENT_DELTA + Consts.SEGMENT_WIDTH)
        self.canvas.create_polygon(points, fill=color, outline='')

    def one(self, color=Colors.RED):
        pass

    def two(self, color=Colors.RED):
        pass

    def three(self, color=Colors.RED):
        points = (self.coords[0] + Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_HEIGHT - Consts.SEGMENT_DELTA,
                  self.coords[1] - Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_HEIGHT - Consts.SEGMENT_DELTA,
                  self.coords[1] - Consts.SEGMENT_WIDTH - Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_HEIGHT - Consts.SEGMENT_WIDTH - Consts.SEGMENT_DELTA,
                  self.coords[0] + Consts.SEGMENT_WIDTH + Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_HEIGHT - Consts.SEGMENT_WIDTH - Consts.SEGMENT_DELTA)
        self.canvas.create_polygon(points, fill=color, outline='')

    def four(self, color=Colors.RED):
        pass

    def five(self, color=Colors.RED):
        pass

    def six(self, color=Colors.RED):
        points = (self.coords[0] + Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_WIDTH,
                  self.coords[0] + Consts.SEGMENT_WIDTH + Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_WIDTH - Consts.SEGMENT_WIDTH,
                  self.coords[1] - Consts.SEGMENT_WIDTH - Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_WIDTH - Consts.SEGMENT_WIDTH,
                  self.coords[1] - Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_WIDTH,
                  self.coords[1] - Consts.SEGMENT_WIDTH - Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_WIDTH + Consts.SEGMENT_WIDTH,
                  self.coords[0] + Consts.SEGMENT_WIDTH + Consts.SEGMENT_DELTA,
                  Consts.DISPLAY_WIDTH + Consts.SEGMENT_WIDTH)
        self.canvas.create_polygon(points, fill=color, outline='')
