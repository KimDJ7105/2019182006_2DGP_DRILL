from pico2d import *

class Grass:
    def __init__(self, _y = 30):
        self.image = load_image('grass.png')
        self.y = _y

    def draw(self):
        self.image.draw(400, self.y)

    def update(self) :
        pass


