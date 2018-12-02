from pico2d import *

import math

import map_stage_1

import game_world

import game_framework

import enemy_die



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
        self.showtime = get_time()
        self.size = 100
        self.bgm = load_music('sound//boss1.mp3')
        self.bgm.set_volume(80)
        if enemy.image is None:
            enemy.image = load_image('enemy_image//stage1_boss.png')

    def update(self):
        if self.hp < 0:
            game_world.remove_object(self)
            die = enemy_die.die(self.x,self.y,100,100)
            game_world.add_object(die, 1)
            self.bgm.stop()
        if self.count == 0:
            if self.x > 0 :
                self.frame = (self.frame + 8 * game_framework.frame_time) % 4

                self.x = self.x + (50 * math.cos(self.radians)) * game_framework.frame_time
                self.y = self.y + (50 * math.sin(self.radians)) * game_framework.frame_time


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
                    game_framework.GameState.life -= 10
            else :
                self.x = self.x + (50 * math.cos(self.radians)) * game_framework.frame_time
                self.y = self.y + (50 * math.sin(self.radians)) * game_framework.frame_time
        else:
            if self.count < get_time() - self.showtime:
                self.count = 0

    def draw(self):
        if self.hp > 200:
            self.image.clip_composite_draw(0, 100 * int(self.frame), 90, 100, self.radians, self.reflect, self.x, self.y,  self.size,  self.size)
        else:
            self.image.clip_composite_draw(90, 100 * int(self.frame), 180, 100, self.radians, self.reflect, self.x, self.y,  self.size,  self.size)

    def get_bb(self):
        return self.x, self.y