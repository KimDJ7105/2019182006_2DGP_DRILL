import play_state
import logo_state
import pico2d

pico2d.open_canvas()

# game main loop code
states = [logo_state,play_state]
for state in states :
    state.enter()
    while state.running :
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()

pico2d.close_canvas()