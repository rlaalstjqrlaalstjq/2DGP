from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('stage_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1565 //2, 400//2)

