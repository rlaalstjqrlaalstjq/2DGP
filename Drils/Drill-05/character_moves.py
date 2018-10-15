from pico2d import *

open_canvas()

grass = load_image('KPU_GROUND')
character = load_image('animation_sheet.png')


def move_run_point1():
    x, y = 0, 0
    frame = 0
    while x < 203:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)

        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.02)
        get_events()

    while y < 535:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y + 30)

        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.02)
        get_events()


move_run_point1()



close_canvas()
