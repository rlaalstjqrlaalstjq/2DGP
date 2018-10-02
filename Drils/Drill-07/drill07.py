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

        delay(0.05)
    elif temp > x:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8

        delay(0.05)

    temp = x


size = 20
x_points = [(random.randint(0,1000)) for n in  range(size)]  #20개 랜덤값 생성
y_points = [(random.randint(0,1000)) for n in  range(size)]
r=1
while True:
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * x_points[r-1] + t * x_points[r]
        y = (1 - t) * y_points[r-1] + t * y_points[r]
        draw(x, y)

    r = (r + 1) % size
    frame = 0

close_canvas()

