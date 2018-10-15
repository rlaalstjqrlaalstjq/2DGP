import game_framework
from pico2d import *
import main_state

name = "Pause_state_2"
image = None

frame = 0

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                frame = 0
                game_framework.pop_state()


def draw():
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()

    if (frame % 400 < 200):
        image.clip_draw(250, 250, 400, 400, 400, 300)

    update_canvas()







def update():
    global frame
    frame = (frame + 1) % 400

def pause():
    pass


def resume():
    pass
