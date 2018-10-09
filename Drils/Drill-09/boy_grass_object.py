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
balls = [BallS() for i in range(random.randint(1,15))] # 작은공 랜덤 갯수 정해주기
ballb = [BallS() for i in range(20-len(balls))]  # 20개중 작은공 갯수 빼서 큰공 갯수 정해주기

running = True;

while running:
    handle_events()

    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw_small() # 작은공 그려주기 실행
        ball.speed()   # 작은공 밑으로 떨어지기 실행

    for ball in ballb:
        ball.draw_big() # 큰공 그려주기 실행
        ball.speed()    # 작은공 밑으로 떨어지기 실행

    update_canvas()

    delay(0.05)

close_canvas()
