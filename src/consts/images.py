from io import BytesIO
from cairosvg import svg2png
from PIL import Image, ImageTk
from os.path import join
from consts.consts import Consts
from consts.states import States


FOLDER = 'resources/images'


class Images:
    def __init__(self):
        self.numbers = [self.load_image(str(i)) for i in range(9)]
        self.mine = self.load_image('mine')
        self.red_mine = self.load_image('red_mine')
        self.flag = self.load_image('flag')
        self.question_mark = self.load_image('question_mark')
        self.covered = self.load_image('covered')
        self.smile = self.load_image('smile')
        self.sunglasses = self.load_image('sunglasses')
        self.dead = self.load_image('dead')

        self.init_dict()

    def init_dict(self):
        self.dict = {}
        for i in range(9):
            self.dict[i] = self.numbers[i]
        self.dict[States.COVERED] = self.covered
        self.dict[States.FLAG] = self.flag
        self.dict[States.QUESTION_MARK] = self.question_mark
        self.dict[States.MINE] = self.mine
        self.dict[States.RED_MINE] = self.red_mine
        self.dict[States.SMILE] = self.smile
        self.dict[States.SUNGLASSES] = self.sunglasses
        self.dict[States.DEAD] = self.dead

    def load_image(self, name, width=Consts.CELL_SIZE, height=Consts.CELL_SIZE):
        bytes = BytesIO()
        svg2png(url=join(FOLDER, name+'.svg'), write_to=bytes, scale=3)
        return ImageTk.PhotoImage(Image.open(bytes).resize((width, height)))
