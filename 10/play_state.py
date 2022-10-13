from pico2d import *
import game_framework
import title_state
import add_delete_boy
import item_state
from random import randint

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = randint(0,800), 90
        self.frame = randint(0,7)
        self.dir = 1 #right
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir*1
        if self.x > 800 :
            self.x = 800
            self.dir = -1 #left
        elif self.x < 0 :
            self.x = 0
            self.dir = 1 #right

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else :
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'Ball' :
            self.ball_image.draw(self.x + 10,self.y + 50)
        elif self.item == 'Bigball' :
            self.big_ball_image.draw(self.x + 10,self.y + 50)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                game_framework.quit();
            elif event.key == SDLK_b :
                game_framework.push_state(add_delete_boy)
            elif event.key == SDLK_i :
                game_framework.push_state(item_state)


boys = None
grass = None
running = False
num = None

def enter() :
    global boys, grass, running, num
    num = 1
    boys = [Boy() for i in range(num)]
    grass = Grass()
    running = True

# finalization code
def exit() :
    global boys, grass
    del boys
    del grass

def update() :
    global num
    for boy in boys:
        boy.update()

def draw_world():
    global num
    grass.draw()
    for boy in boys:
        boy.draw()

def draw() :
    clear_canvas()
    draw_world()
    update_canvas()

def pause() :
    pass

def resume() :
    pass