from pico2d import *
import math

open_canvas(800,600)

grass = load_image('grass.png')
character = load_image('character.png')

rec = True

while (True):
    if rec is False :
        x = 0
        y = 90
        while (x < 770) :
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,90)
            x = x + 2
            delay(0.01)
        while(y < 570) :
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y + 2
            delay(0.01)
        while(x > 30) :
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x = x - 2
            delay(0.01)
        while(y > 90) :
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y = y - 2
            delay(0.01)

        rec = True
    else :
        angle = -90
        while(angle < -82) :
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400 + (math.cos(angle) * 200), 300 + (math.sin(angle)*200))
            angle = angle + 0.05
            delay(0.01)
        rec = False

close_canvas()
