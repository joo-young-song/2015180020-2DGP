from pico2d import *
import os
import math
import map_stage_1
import map_stage_2
import map_stage_3


os.chdir('D:\\2DGM\\2DGP\\2015180020-2DGP\\2DGP project\\2주차 적구현')


open_canvas()

pig = None

Grass = map_stage_2.Grass()

Tile = map_stage_2.Tile()


class enemy:
    image = None
    def __init__(self):
        self.x = 0
        self.y = 550
        self.hp = 10
        self.radians = 0.0
        self.Xmove = 0.0
        self.Ymove = 1.0
        self.head = 0
        self.frame = 0
        self.Tile_Spot_x = 0
        self.Tile_Spot_y = 0

        if enemy.image == None:
            enemy.image = load_image('stage1_pig1.png')
    def update(self):
        self.frame = (self.frame + 1) % 7

        self.x = self.x + 5 * math.cos(self.radians)
        self.y = self.y + 5 * math.sin(self.radians)


       


        delay(0.05)
    def draw(self):
        self.image.clip_composite_draw(0,100 + 100*self.frame,100,100,self.radians,'',self.x, self.y,100,100)



pig = enemy()





while True:

    clear_canvas()

    Grass.draw()

    Tile.draw()

    pig.draw()

    pig.update()

    update_canvas()