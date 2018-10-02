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


size = 20
points = [(random.randint(100,200)) for n in  range(size)]  #20개 랜덤값 생성


while True:

    pass


