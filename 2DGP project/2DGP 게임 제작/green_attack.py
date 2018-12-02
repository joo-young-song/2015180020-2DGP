from pico2d import *
import math
import game_world
import game_framework

class fire:
    lazer_start = None
    lazer_middle = None
    lazer_last = None

    def __init__(self, x = 0, y = 0, radians = 0.0, lazer_part = 0, show = 0):
        self.x = x
        self.y = y
        self.radians = radians
        self.lazer_part = lazer_part
        self.count = show
        self.showtime = get_time()
        if fire.lazer_start is None:
            fire.lazer_start = load_image('bullet_image//lazer_start.png') # 36 92
        if fire.lazer_middle is None:
            fire.lazer_middle = load_image('bullet_image//lazer_middle.png') # 100 100
        if fire.lazer_last is None:
            fire.lazer_last = load_image('bullet_image//lazer_last.png') # w 48 h 100

    def update(self):
        if self.x < 0 or self.x > 800 or self.y < 0 or self.y > 700:
            game_world.remove_object(self)
        if self.count == 0:
            self.x = self.x + 400*math.cos(self.radians)*game_framework.frame_time
            self.y = self.y + 400*math.sin(self.radians)*game_framework.frame_time
            for gets in game_world.enemy_objects():
                if gets.hp >= 0:
                    if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < gets.size - 10:
                        game_world.remove_object(self)
                        gets.hp -= 3
                        break
        else:
            if self.count < get_time() - self.showtime:
                self.count = 0



    def draw(self):
        if self.count == 0:
            if self.lazer_part == 0:
                self.lazer_start.clip_composite_draw(0, 0, 36, 92, self.radians, 'hv', self.x, self.y, 23, 50)
            elif self.lazer_part == 1:
                self.lazer_middle.clip_composite_draw(0, 0, 100, 100, self.radians, '', self.x, self.y, 27, 50)
            elif self.lazer_part == 2:
                self.lazer_last.clip_composite_draw(0, 0, 48, 100, self.radians, 'hv', self.x, self.y, 25, 50)


