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
        pass
    # draw p2-p3
    for i in range(0, 100, 2):
        pass
    # draw p3-p4
    for i in range(0, 100, 2):
        pass
    for i in range(0, 100, 2):
        pass
        # draw p5-p6
    for i in range(0, 100, 2):
        pass
        # draw p6-p7
    for i in range(0, 100, 2):
        pass
        # draw p7-p8
    for i in range(0, 100, 2):
        pass
        # draw p8-p9
    for i in range(0, 100, 2):
        pass
        # draw p9-p10
    for i in range(0, 100, 2):
       pass
        # draw p10-p1
    for i in range(0, 100, 2):
        pass

close_canvas()
