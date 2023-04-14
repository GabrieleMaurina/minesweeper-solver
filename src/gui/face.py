import tkinter as tk
from consts.consts import Consts
from consts.colors import Colors
from emoji import emojize

from PIL import Image, ImageDraw, ImageTk


WIDTH = 40
HEIGHT = 40
RADIUS = 18
EYE_RADIUS = 3
EYE_OFFSET = 6
EYE_ELEVATION = 2


class Face:
    def __init__(self, home):
        self.home = home
        self.button = tk.Button(
            self.home.menu_frame, font=self.home.gui.font, borderwidth=Consts.SMALL_BORDER, text=emojize('🙂'))
        self.button = tk.Label(
            self.home.menu_frame, borderwidth=Consts.SMALL_BORDER, text=emojize('🙂'))
        # self.create_smile()

    def circle(self, draw, center, radius, **kwargs):
        x, y = center
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), **kwargs)

    def create_smile(self):
        img = Image.new('RGBA', (WIDTH, WIDTH), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # self.circle(draw, (WIDTH/2, HEIGHT/2), RADIUS,
        #             outline=Colors.BLACK, fill=Colors.YELLOW)
        # self.circle(draw, (WIDTH/2-EYE_OFFSET, HEIGHT/2-EYE_ELEVATION),
        #             EYE_RADIUS, fill=Colors.BLACK)
        # self.circle(draw, (WIDTH/2+EYE_OFFSET, HEIGHT/2-EYE_ELEVATION),
        #             EYE_RADIUS, fill=Colors.BLACK)
        draw.arc((10, 10, 30, 30), 10, 170, fill=Colors.BLACK, width=2)
        img.show()
        exit(0)

    def grid(self, *args, **kwargs):
        self.button.grid(*args, **kwargs)
