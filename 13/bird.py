from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 5

class RUN:
    def enter(self, event):
        self.change = False
        pass

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 5
        if int(self.frame) == 4 :
            self.change = True
        if int(self.frame) == 0 and self.change == True:
            self.change = False
            self.line = (self.line + 1) % 3

        if self.line == 0 and int(self.frame) == 4:
            self.draw_frame = 3
        else :
            self.draw_frame = int(self.frame)

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 800 :
            self.dir = -1
        elif self.x < 0 :
            self.dir = 1

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(self.draw_frame*181, self.line * 170, 181, 170,0,'h', self.x, self.y, 150, 100)
        elif self.dir == 1:
            self.image.clip_composite_draw(self.draw_frame*181, self.line * 170, 181, 170,0,'',self.x, self.y, 150 , 100)

#3. 상태 변환 구현
class Bird:

    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.draw_frame = 0
        self.line = 2
        self.dir = 1
        
        self.change = None
        if Bird.image == None :
            Bird.image = load_image('bird_animation.png')

        self.event_que = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

