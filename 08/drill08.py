from pico2d import *


def handle_events():
    global running
    global x
    global y
    global x_dir
    global y_dir
    global last_way
    events = get_events()
    for event in events :
        if event.type == SDL_QUIT :
            running = False
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_RIGHT :
                x_dir += 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
            elif event.key == SDLK_UP :
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_ESCAPE :
                running = False
        elif event.type == SDL_KEYUP :
            if event.key == SDLK_RIGHT :
                last_way = 1
                x_dir -= 1
            elif event.key == SDLK_LEFT :
                last_way = -1
                x_dir += 1
            elif event.key == SDLK_UP :
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                y_dir += 1
    pass


open_canvas()
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 600 // 2
frame = 0
x_dir = 0
y_dir = 0
last_way = 1;

while running:
    clear_canvas()
    if x_dir == 0 and y_dir == 0:
        if last_way == 1 :
            character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
        elif last_way == -1 :
            character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    elif x_dir == 1 :
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif x_dir == -1 :
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    if y_dir == 1 or y_dir == -1 :
        if last_way == 1 :
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif last_way == -1 :
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    if x_dir == 1 and x < 800 :
        x += x_dir * 5
    elif x_dir == -1 and x > 0 :
        x += x_dir * 5
    if y_dir == 1 and y < 600 :
        y += y_dir*5
    elif y_dir == -1 and y > 0 :
        y += y_dir*5

    delay(0.01)

close_canvas()
