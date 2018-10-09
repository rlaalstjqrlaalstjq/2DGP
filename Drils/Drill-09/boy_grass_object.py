from pico2d import *
import random


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700) , 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame +1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class BallS:
    def __init__(self):
        self.x, self.y = random.randint(50,750) , 600
        self.down = random.randint(2, 10)  # 랜덤값으로 속도 정해주기
        self.image = load_image('ball21x21.png')   # 작은공 이미지 로드
        self.images = load_image('ball41x41.png') # 큰공 이미지 로드

    def draw_small(self):
            self.image.clip_draw(0, 0, 21, 21, self.x, self.y)  #작은공 그려주기

    def draw_big(self):
            self.images.clip_draw(0, 0, 41, 41, self.x, self.y) #큰공 그려주기

    def speed(self):  # 공이 밑으로 떨어지는 행위
        if self.y > 40:
            self.y = self.y - self.down
        else:
            self.y = 40


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

team = [Boy() for i in range(11)]
grass = Grass()

running = True;

while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    update_canvas()

    delay(0.05)

close_canvas()
