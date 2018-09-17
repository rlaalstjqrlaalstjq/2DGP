from pico2d import *

open_canvas()

grass = load_image('grass.png')
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


def move_run_point2():
    x, y = 203, 535
    frame = 0
    while x > 132:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.02)
        get_events()

    while y > 243:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.02)
        get_events()


def move_run_point3():
    x, y = 132, 243
    frame = 0
    while x < 535:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.02)
        get_events()

    while y < 470:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.02)
        get_events()


def move_run_point4():
    x, y = 535, 470
    frame = 0
    while x > 477:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.02)
        get_events()

    while y > 203:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.02)
        get_events()


def move_run_point5():
    x, y = 477, 203;
    frame = 0
    while x < 715:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.02)
        get_events()

    while y > 136:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.02)
        get_events()


def move_run_point6():
    x, y = 715, 136
    frame = 0
    while x > 316:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.02)
        get_events()

    while y < 225:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.02)
        get_events()


def move_run_point7():
    x, y = 316, 225;
    frame = 0
    while x < 510:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.02)
        get_events()

    while y > 92:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.02)
        get_events()


def move_run_point8():
    x, y = 510, 92
    frame = 0
    while x < 692:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.02)
        get_events()

    while y < 518:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.02)
        get_events()


def move_run_point9():
    x, y = 692, 518
    frame = 0
    while x > 682:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.02)
        get_events()

    while y > 336:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.02)
        get_events()


def move_run_point10():
    x, y = 682, 336
    frame = 0
    while x < 712:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.02)
        get_events()

    while y < 349:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)

        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.02)
        get_events()


move_run_point1()

while True:
    move_run_point2()
    move_run_point3()
    move_run_point4()
    move_run_point5()
    move_run_point6()
    move_run_point7()
    move_run_point8()
    move_run_point9()
    move_run_point10()

close_canvas()
