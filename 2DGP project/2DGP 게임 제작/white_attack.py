from pico2d import *
import stage_1
import math
import game_world

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
        self.x = self.x + 10*math.cos(self.radians)
        self.y = self.y + 10*math.sin(self.radians)
        self.frame = (self.frame+1) % 3
        for gets in game_world.enemy_objects():
            if gets.hp >= 0:
                if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < 40:
                    game_world.remove_object(self)
                    gets.hp -= 11
                    if gets.hp < 0:
                        game_world.remove_object(gets)
                    break


    def draw(self):
        self.image.clip_composite_draw(0, 16 + 16 + self.frame, 16, 16, self.radians, self.reflect, self.x, self.y, 10, 10)


