import game_framework
import pico2d

import play_state
import main_state

# pico2d.open_canvas(400, 300)
pico2d.open_canvas(1000, 1000)
game_framework.run(main_state)
pico2d.close_canvas()