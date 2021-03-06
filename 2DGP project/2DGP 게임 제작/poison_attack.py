from pico2d import *
import math
import game_world
import random
import game_framework

class fire:
    image = None

    def __init__(self, x = 0, y = 0, radians = 0.0):
        self.x = x
        self.y = y
        self.radians = radians
        self.reflect = ''
        self.bullet_color = random.randint(0, 12)
        self.frame = 0
        if fire.image is None:
            fire.image = load_image('bullet_image//poison_bullet.png')

    def update(self):
        self.x = self.x + 300*math.cos(self.radians)*game_framework.frame_time
        self.y = self.y + 300*math.sin(self.radians)*game_framework.frame_time
        self.frame = (self.frame + 16 * game_framework.frame_time) % 8
        if self.frame > 6:
            game_world.remove_object(self)
        for gets in game_world.enemy_objects():
            if gets.hp >= 0 and gets.x > 0:
                if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < gets.size - 20:
                    gets.poison_condition = 6
                    gets.poison_time = get_time()

    def draw(self):
        self.image.clip_composite_draw(0, 32 * int(self.frame), 32, 32, self.radians, self.reflect, self.x, self.y, 32, 32)


