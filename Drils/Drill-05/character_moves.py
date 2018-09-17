from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_point1():
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
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.02)
        get_events()


def move_point2():
    pass


def move_point3():
    pass


def move_point4():
    pass


def move_point5():
    pass


def move_point6():
    pass


def move_point7():
    pass


def move_point8():
    pass


def move_point9():
    pass


def move_point10():
    pass


while True:
    move_point1()
    move_point2()
    move_point3()
    move_point4()
    move_point5()
    move_point6()
    move_point7()
    move_point8()
    move_point9()
    move_point10()

close_canvas()
