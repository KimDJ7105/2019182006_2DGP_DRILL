from pico2d import *
import game_framework

from grass import Grass
from boy import Boy
import game_world


boy = None
grass1 = None
grass2 = None
ball = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass1, grass2
    boy = Boy()
    grass1 = Grass()
    grass2 = Grass(50)
    game_world.add_object(boy, 1)
    game_world.add_object(grass1, 2)
    game_world.add_object(grass2, 0)

# 종료
def exit():
    global boy, grass1, grass2
    del boy
    del grass1
    del grass2

def update():
    for o in game_world.all_objects():
        o.update()

def draw():
    clear_canvas()
    for o in game_world.all_objects():
        o.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
