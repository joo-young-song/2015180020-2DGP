from pico2d import *
import math
import game_world
import game_framework

class fire:
    image = None

    def __init__(self, x = 0, y = 0, radians = 0.0):
        self.x = x
        self.y = y
        self.radians = radians
        self.reflect = ''
        self.frame = 0
        if fire.image is None:
            fire.image = load_image('bullet_image//attack_1.png')

    def update(self):
        self.x = self.x + 250*math.cos(self.radians)*game_framework.frame_time
        self.y = self.y + 250*math.sin(self.radians)*game_framework.frame_time
        self.frame = (self.frame+6*game_framework.frame_time) % 3
        for gets in game_world.enemy_objects():
            if gets.hp >= 0 and gets.x > 0:
                if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < gets.size - 10:
                    game_world.remove_object(self)
                    gets.hp -= 11
                    break


    def draw(self):
        self.image.clip_composite_draw(0, 16 * int(self.frame), 16, 16, self.radians, self.reflect, self.x, self.y, 20, 20)


