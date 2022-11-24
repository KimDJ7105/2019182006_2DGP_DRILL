from pico2d import *
import server

class Ball:
    image = None
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
        if Ball.image == None :
            Ball.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self) :
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        Ball.image.draw(sx,sy)
        pass

    def handle_collision(self, _a, _group) :
        pass

    def get_bb(self):
        return self.x - 23//2, self.y - 23//2, self.x + 23//2, self.y + 23//2