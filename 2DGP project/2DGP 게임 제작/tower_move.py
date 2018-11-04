from pico2d import *
import game_world
import math
import map_stage_1
import map_stage_2
import map_stage_3

class tower:
    image = None

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.radians = 0.0
        self.frame = 0
        self.attack_speed = 0
        self.reflect = ''
        self.attack = False
        self.range = 300
        if tower.image is None:
            tower.image = load_image('white_tower.png')

    def update(self):
        if self.attack == False:
            self.frame = (self.frame + 1) % 4
        else:
            self.frame = (self.frame + 1) % 2

    def attack_range(self):
        for enemy_object in game_world.all_objects():
            if math.sqrt( (self.x - enemy_object.x) * (self.y - enemy_object.y) + (self.y - enemy_object.y) * (self.y - enemy_object.y) < self.range):
                self.attack = True

    def draw(self):
        if self.attack == False:
            self.image.clip_composite_draw(0, 100 + 100 * self.frame, 100, 100, self.radians, self.reflect, self.x, self.y, 100, 100)

        else :
            self.image.clip_composite_draw(0, 100 + 100 * (self.frame + 4), 100, 100, self.radians, self.reflect, self.x, self.y, 100, 100)


