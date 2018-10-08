from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
frame = 0
temp = 0


def draw(x,y):
    global frame
    global temp

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if temp < x:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

        delay(0.07)
    elif temp > x:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

        delay(0.07)

    temp = x




size = 10
x_p1 = [(random.randint(0, 1000)) for i in range(size)]
y_p1 = [(random.randint(0, 1000)) for i in range(size)]


while True:
    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * x_p1[0] + (-4 * t ** 2 + 4 * t) * x_p1[1] + (2 * t ** 2 - t) * x_p1[2]
        y = (2 * t ** 2 - 3 * t + 1) * y_p1[0] + (-4 * t ** 2 + 4 * t) * y_p1[1] + (2 * t ** 2 - t) * y_p1[2]
        draw(x,y)

    frame = 0
    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[2] + (t ** 3 - t ** 2) * x_p1[3]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[2] + (t ** 3 - t ** 2) * y_p1[3]) / 2
        draw(x, y)

    frame = 0
    # draw p3-p4
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[2] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[3] + (t ** 3 - t ** 2) * x_p1[4]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[2] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[3] + (t ** 3 - t ** 2) * y_p1[4]) / 2
        draw(x, y)

    frame = 0
    # draw p4-p5
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[2] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[3] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[4] + (t ** 3 - t ** 2) * x_p1[5]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[2] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[3] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[4] + (t ** 3 - t ** 2) * y_p1[5]) / 2
        draw(x, y)

    frame = 0
        # draw p5-p6
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[3] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[4] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[5] + (t ** 3 - t ** 2) * x_p1[6]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[3] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[4] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[5] + (t ** 3 - t ** 2) * y_p1[6]) / 2
        draw(x, y)

    frame = 0
        # draw p6-p7
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[5] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[6] + (t ** 3 - t ** 2) * x_p1[7]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[5] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[6] + (t ** 3 - t ** 2) * y_p1[7]) / 2
        draw(x, y)

    frame = 0
        # draw p7-p8
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[6] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[7] + (t ** 3 - t ** 2) * x_p1[8]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[6] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[7] + (t ** 3 - t ** 2) * y_p1[8]) / 2
        draw(x, y)

    frame = 0
        # draw p8-p9
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[6] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[7] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[8] + (t ** 3 - t ** 2) * x_p1[9]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[6] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[7] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[8] + (t ** 3 - t ** 2) * y_p1[9]) / 2
        draw(x, y)

    frame = 0
        # draw p9-p10
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[8] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[9] + (t ** 3 - t ** 2) * x_p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[8] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[9] + (t ** 3 - t ** 2) * y_p1[0]) / 2
        draw(x, y)

    frame = 0
        # draw p10-p1
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * x_p1[8] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_p1[9] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_p1[0] + (t ** 3 - t ** 2) * x_p1[1]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * y_p1[8] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_p1[9] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_p1[0] + (t ** 3 - t ** 2) * y_p1[1]) / 2
        draw(x, y)

    frame = 0

close_canvas()
#최종완성