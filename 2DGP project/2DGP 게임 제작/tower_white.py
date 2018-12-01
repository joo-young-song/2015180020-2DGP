from pico2d import *
import game_world
import math
import white_attack
import game_framework
import stage_1



class tower_w:
    image = None

    def __init__(self, x=0, y=0, set=False):
        self.x = x
        self.y = y
        self.radians = 0.0
        self.frame = 5
        self.attack_speed = 2
        self.reflect = ''
        self.attack = False
        self.set = set
        self.range = 300
        self.shottime = get_time()
        if tower_w.image is None:
            tower_w.image = load_image('tower_image//white_tower.png')

    def update(self):
        if self.set == False:
            self.frame = (self.frame + 8 * game_framework.frame_time) % 4
        elif self.set == True:
            self.attack = False
            for gets in game_world.enemy_objects():
                if gets.hp >= 0 and gets.x > 0:
                    if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < self.range:
                        self.radians = math.atan2((gets.y - self.y),(gets.x - self.x))
                        self.attack = True
                        break
                else:
                    self.attack = False

            if self.attack == True:
                self.frame = (self.frame + 2 * game_framework.frame_time) % 2
                if self.attack_speed < get_time() - self.shottime:
                    fire = white_attack.fire(self.x, self.y, self.radians)
                    game_world.add_object(fire, 1)
                    self.shottime = get_time()

            else:
                self.frame = (self.frame + 8 * game_framework.frame_time) % 4






    def draw(self):
        if self.attack == False:
            self.image.clip_composite_draw(0, 50 * int(self.frame + 2), 50, 50, self.radians, self.reflect, self.x, self.y, 50, 50)
        else:
            self.image.clip_composite_draw(0, 50 * int(self.frame), 50, 50, self.radians, self.reflect, self.x,
                                           self.y, 50, 50)


    def get_bb(self):
        return self.x, self.y, self.range
