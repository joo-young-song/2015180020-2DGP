from pico2d import *

import game_world

import game_framework

class die:
    image = None

    def __init__(self, x = 0, y = 0, sizex = 0, sizey = 0):
        self.x = x
        self.y = y
        self.width = sizex
        self.height = sizey
        self.hp = 10
        self.frame = 0

        if die.image is None:
            die.image = load_image('enemy_image//enemy_die.png')

    def update(self):
        self.frame = (self.frame + 10 * game_framework.frame_time) % 5
        if self.frame > 3:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_composite_draw(0, 117 * int(self.frame), 127, 117, 0, '', self.x, self.y, self.width, self.height)