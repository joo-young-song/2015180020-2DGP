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
        if fire.image is None:
            fire.image = load_image('bullet_image//ninja_bullet.png')

    def update(self):
        if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 700:
            game_world.remove_object(self)
        self.x = self.x + 350*math.cos(self.radians)*game_framework.frame_time
        self.y = self.y + 350*math.sin(self.radians)*game_framework.frame_time
        for gets in game_world.enemy_objects():
            if gets.hp >= 0 and gets.x > 0:
                if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < gets.size - 40:
                    game_world.remove_object(self)
                    gets.hp -= self.bullet_color/2
                    break


    def draw(self):
        self.image.clip_composite_draw(0, 22 * self.bullet_color, 22, 22, self.radians, self.reflect, self.x, self.y, 22, 22)


