from pico2d import *
import os

os.chdir('D:\\2DGM\\2DGP\\2015180020-2DGP\\2DGP project\\2주차 적구현')


pig = None

open_canvas()

class enemy:
    def __init__(self):
        self.x = 300
        self.y = 0
        self.hp = 10
        self.head = 1
        self.Xmove = 0
        self.Ymove = 1
        self.frame = 0
        self.image = load_image('pig_first.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x = self.x + self.Xmove
        self.y = self.y + self.Ymove
        delay(0.05)
    def draw(self):
        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.head == 0:
            self.image.rotate_draw(0,self.x,self.y)
        elif self.head == 1:
            self.image.rotate_draw(1.57,self.x,self.y)


pig = enemy()





while True:

    clear_canvas()

    pig.draw()

    pig.update()

    update_canvas()