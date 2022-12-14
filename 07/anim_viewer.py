from pico2d import *

open_canvas()

player = load_image('man.png')
grass = load_image('grass.png')

#transform func start
def early_transform() :
    for x in range(0,2):
        clear_canvas()
        grass.draw(400,30)
        if x == 0 :
            player.clip_draw(50, 184, 30,92, 400, 90)
        else :
            player.clip_draw(85, 184, 30,92, 400, 90)
        update_canvas()
        delay(0.5)

def next_transform() :
    for frame in range(0,3) :
        clear_canvas()
        grass.draw(400,30)
        player.clip_draw(120 +((frame)*50) ,184,50,92,400,90)
        update_canvas()
        delay(0.3)

def end_transform() :
    for x in range(0,3):
        clear_canvas()
        grass.draw(400,30)
        if x == 0 :
            player.clip_draw(270, 184, 55,92, 400, 90)
        elif x == 1 :
            player.clip_draw(330, 184, 50,92, 400, 90)
        elif x == 2 :
            player.clip_draw(378, 184, 50,92, 400, 90)
        update_canvas()
        delay(0.5)

def transform():
    early_transform()
    next_transform()
    end_transform()

#transform func end

def move_to_origin() : #character teleport (0,0) (not actually)
    for x in (400, 395, 405, 395, 50, 45, 50, 55 ):
        clear_canvas()
        grass.draw(400,30)
        player.clip_draw(378, 184, 50,92, x, 90)
        update_canvas()
        delay(0.03)

#attack start
def attack1() :
    frame = 0
    for x in (50, 75, 90):
        clear_canvas()
        grass.draw(400,30)
        if frame != 2:
            player.clip_draw(10 + (frame * 60), 92, 60,92, x, 90)
        elif frame == 2 :
            player.clip_draw(130, 92, 85,92, x, 90)
        frame += 1
        update_canvas()
        delay(0.1)

def attack2() :
    frame = 0
    for x in (90, 160):
        clear_canvas()
        grass.draw(400,30)
        player.clip_draw(220 + (frame * 60), 92, 60,92, x, 90)
        update_canvas()
        frame += 1;
        delay(0.2)

def attack3() :
    frame = 0
    for x in range (170, 400 + 1, 5) :
        clear_canvas()
        grass.draw(400,30)
        player.clip_draw(190 + (frame)*70 , 0, 68,92, x, 90)
        update_canvas()
        frame = (frame + 1) % 3
        delay(0.05)

def end_attack() :
    frame = 0
    for num in range (0,3) :
        clear_canvas()
        grass.draw(400,30)
        player.clip_draw(10 + (frame)*60 , 0, 60,92, 400, 90)
        update_canvas()
        frame += 1
        delay(0.5)

def attack() :
    attack1()
    attack2()
    attack3()

#attack stop

def back_transform() :
    for x in range(0,3):
        clear_canvas()
        grass.draw(400,30)
        if x == 2 :
            player.clip_draw(270, 184, 55,92, 400, 90)
        elif x == 1 :
            player.clip_draw(330, 184, 50,92, 400, 90)
        elif x == 0 :
            player.clip_draw(378, 184, 50,92, 400, 90)
        update_canvas()
        delay(0.5)
    
    for frame in range(0, 3) :
        clear_canvas()
        grass.draw(400,30)
        player.clip_draw(220 - ((frame)*50) ,184,50,92,400,90)
        update_canvas()
        delay(0.3)
    
    for x in range(0,2):
        clear_canvas()
        grass.draw(400,30)
        if x == 1 :
            player.clip_draw(50, 184, 30,92, 400, 90)
        else :
            player.clip_draw(85, 184, 30,92, 400, 90)
        update_canvas()
        delay(0.5)

while(True) :
    transform()
    move_to_origin()
    attack()
    back_transform()
    get_events()
    break; #if you want loop, exclude this


close_canvas()
