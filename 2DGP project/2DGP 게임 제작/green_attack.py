from pico2d import *
import stage_1
import math
import game_world

class fire:
    lazer_start = None
    lazer_middle = None
    lazer_last = None

    def __init__(self, x = 0, y = 0, radians = 0.0, lazer_part = 0):
        self.x = x
        self.y = y
        self.radians = radians
        self.reflect = ''
        self.lazer_part = lazer_part
        if fire.lazer_start is None:
            fire.lazer_start = load_image('lazer_start.png') # 36 92
        if fire.lazer_middle is None:
            fire.lazer_middle = load_image('lazer_middle.png') # 100 100
        if fire.lazer_last is None:
            fire.lazer_last = load_image('lazer_last.png') # w 48 h 100

    def update(self):
        self.x = self.x + 10*math.cos(self.radians)
        self.y = self.y + 10*math.sin(self.radians)
        for gets in stage_1.enemy_1:
            if gets.hp >= 0:
                if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < 40:
                    game_world.remove_object(self)
                    gets.hp -= 5
                    if gets.hp < 0:
                        game_world.remove_object(gets)
                    break


    def draw(self):
        if self.lazer_part == 0:
            self.lazer_start.clip_composite_draw(0, 0, 36, 92, self.radians, self.reflect, self.x, self.y, 10, 10)
        elif self.lazer_part == 1:
            self.lazer_middle.clip_composite_draw(0, 0, 100, 100, self.radians, self.reflect, self.x, self.y, 10, 10)
        elif self.lazer_part == 2:
            self.lazer_last.clip_composite_draw(0, 0, 48, 100, self.radians, self.reflect, self.x, self.y, 10, 10)


