from pico2d import *

import math

import map_stage_1

open_canvas()

pig = None

Grass = map_stage_1.Grass()

Tile = map_stage_1.Tile()



class enemy:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 300
        self.hp = 10
        self.radians = 0.0
        self.head = 0
        self.frame = 0
        self.reflect = ''
        if enemy.image is None:
            enemy.image = load_image('stage1_pig1.png')

    def update(self):
        self.frame = (self.frame + 1) % 7

        self.x = self.x + 5 * math.cos(self.radians)
        self.y = self.y + 5 * math.sin(self.radians)

        if map_stage_1.tile_rotate[int(self.y // 50)][int(self.x // 50)] == 1:
            self.radians = 3.14
            self.reflect = "hv"
        elif map_stage_1.tile_rotate[int(self.y // 50)][int(self.x // 50)] == 2:
            self.radians = -1.57
            self.reflect = ''
        elif map_stage_1.tile_rotate[int(self.y // 50)][int(self.x // 50)] == 3:
            self.radians = 0
            self.reflect = ''
        elif map_stage_1.tile_rotate[int(self.y // 50)][int(self.x // 50)] == 4:
            self.radians = 1.57
            self.reflect = ''
        delay(0.05)

    def draw(self):
        self.image.clip_composite_draw(0, 100 + 100 * self.frame, 100, 100, self.radians, self.reflect, self.x, self.y, 100, 100)