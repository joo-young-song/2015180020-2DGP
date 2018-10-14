from pico2d import *
import os

os.chdir('D:\\2DGM\\2DGP\\2015180020-2DGP\\2DGP project\\2주차 적구현')


pig = None

class enemy:
    def __init__(self):
        self.x = 0
        self.y = 300
        self.hp = 10
        self.head = 0
        self.Xmove = 1
        self.Ymove = 0
        self.frame = 0
        self.image = load_image('pig_first.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x = self.x + self.Xmove
        self.y = self.y + self.Ymove
    def draw(self):
        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.head == 0:
            self.image.rotate_draw(0,self.x,self.y)
        elif self.head == 1:
            self.image.rotate_draw(90,self.x,self.y)


pig = enemy()


open_canvas()


while True:

    clear_canvas()

    pig.draw()

    pig.update()

    update_canvas()