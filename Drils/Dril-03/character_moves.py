from pico2d import *

import math

# os.chdir('C:\\Users\김민섭\\Desktop\\2D 프로그래밍\\2018-2DGP\\Labs\\Lecture03')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def make_rectangle():
    def move_from_center_to_right():
        x, y = 800 // 2, 90
        while x < 800 - 25:
            clear_canvas_now()
            grass.draw_now(400, 30)
            chracter.draw_now(x, y)
            x += 2
            delay(0.01)

    def move_up():
        x, y = 800 - 25, 90
        while y < 600 - 50:
            clear_canvas_now()
            grass.draw_now(400, 30)
            chracter.draw_now(x, y)
            y += 2
            delay(0.01)

    def move_left():
        x, y = 800 - 25, 550
        while x > 0 + 25:
            clear_canvas_now()
            grass.draw_now(400, 30)
            chracter.draw_now(x, y)
            x -= 2
            delay(0.01)

    def move_from_center_to_left():
        x, y = 0 + 25, 550
        while y > 0 + 25:
            clear_canvas_now()
            grass.draw_now(400, 30)
            chracter.draw_now(x, y)
            y -= 2
            delay(0.01)

    def move_down():
        pass

    move_from_center_to_right()
    move_up()
    move_left()
    move_from_center_to_left()
    move_down()

def make_circle():
    cx,cy,r = 800 // 2,600 // 2,(600 - 180) // 2
    degree = -90
    while degree<270:
        radian = math.radians(degree)
        x = cx + r * math.cos(radian)
        y = cy + r * math.sin(radian)
        clear_canvas_now()
        grass.draw_now(400, 30)
        chracter.draw_now(x, y)
        degree += 1
        delay(0.01)


while True:
    #make_rectangle()
    make_circle()

close_canvas()
