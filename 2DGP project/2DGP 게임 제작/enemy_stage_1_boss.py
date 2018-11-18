from pico2d import *

import math

import map_stage_1

import game_world

open_canvas()

pig = None

class enemy:
    image = None

    def __init__(self, show = 0):
        self.x = -100
        self.y = 300
        self.hp = 450
        self.radians = 0.0
        self.head = 0
        self.frame = 0
        self.reflect = ''
        self.count = show
        if enemy.image is None:
            enemy.image = load_image('enemy_image//stage1_boss.png')

    def update(self):
        if self.hp == 0:
            game_world.remove_object(self)
        if self.count == 0 :
            if self.x > 0 :
                self.frame = (self.frame + 1) % 4

                self.x = self.x + 1 * math.cos(self.radians)
                self.y = self.y + 1 * math.sin(self.radians)

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
                elif map_stage_1.tile_rotate[int(self.y // 50)][int(self.x // 50)] == 5:
                    game_world.remove_object(self)


            else :
                self.x = self.x + 5 * math.cos(self.radians)
                self.y = self.y + 5 * math.sin(self.radians)

        else :
            self.count -= 1

    def draw(self):
        if self.hp > 200:
            self.image.clip_composite_draw(0, 100 * self.frame, 90, 100, self.radians, self.reflect, self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(90, 100 * self.frame, 180, 100, self.radians, self.reflect, self.x, self.y, 100, 100)

    def get_bb(self):
        return self.x, self.y