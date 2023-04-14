from io import BytesIO
from cairosvg import svg2png
from PIL import Image
from os.path import join
from consts.consts import Consts


FOLDER = 'resources/images'


class Images:
    def __init__(self):
        self.numbers = [self.load_image(str(i)) for i in range(9)]
        self.mine = self.load_image('mine')
        self.red_mine = self.load_image('red_mine')
        self.flag = self.load_image('flag')
        self.questionmark = self.load_image('question_mark')
        self.covered = self.load_image('covered')
        self.smile = self.load_image('smile')
        self.sunglasses = self.load_image('sunglasses')
        self.dead = self.load_image('dead')

    def load_image(self, name):
        bytes = BytesIO()
        svg2png(url=join(FOLDER, name+'.svg'), write_to=bytes, scale=3)
        return Image.open(bytes).resize((Consts.CELL_SIZE, Consts.CELL_SIZE))


Images = Images()

exit(0)
