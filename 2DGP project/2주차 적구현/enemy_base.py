from pico2d import *
import os
import math

os.chdir('D:\\2DGM\\2DGP\\2015180020-2DGP\\2DGP project\\2주차 적구현')


pig = None

open_canvas()

class enemy:
    def __init__(self):
        self.x = 0
        self.y = 300
        self.hp = 10
        self.radians = 0.0
        self.Xmove = 0.0
        self.Ymove = 1.0
        self.head = 0
        self.frame = 0
        self.image = load_image('pig_first.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x = self.x + 5*math.cos(self.radians)
        self.y = self.y + 5*math.sin(self.radians)
        delay(0.05)
    def draw(self):
        self.image.rotate_draw(self.radians,self.x,self.y)


pig = enemy()





while True:

    clear_canvas()

    pig.draw()

    pig.update()

    update_canvas()