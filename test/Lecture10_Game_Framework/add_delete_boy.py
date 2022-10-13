from pico2d import *
import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('add_delete_boy.png')


def exit():
    global image
    del image

def update():
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE :
                game_framework.pop_state();
            elif event.key == SDLK_KP_PLUS:
                play_state.num += 1
                play_state.boys.append(play_state.Boy())
                pass
            elif event.key == SDLK_KP_MINUS:
                if play_state.num > 1 :
                    play_state.num -= 1
                    play_state.boys.pop(-1)
                pass
