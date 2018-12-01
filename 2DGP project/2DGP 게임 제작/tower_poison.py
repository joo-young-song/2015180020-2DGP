from pico2d import *
import game_world
import math
import poison_attack
import game_framework
import stage_1



class tower_p:
    image = None

    def __init__(self, x=0, y=0, set=False):
        self.x = x
        self.y = y
        self.radians = 0.0
        self.frame = 4
        self.attack_speed = 0.1
        self.reflect = ''
        self.attack = False
        self.set = set
        self.range = 100
        self.shottime = get_time()
        if tower_p.image is None:
            tower_p.image = load_image('tower_image//poison_tower.png')

    def update(self):
        if self.set == False:
            self.frame = (self.frame + 8 * game_framework.frame_time) % 4
            events = get_events()
            for event in events:
                if event.type == SDL_MOUSEMOTION:
                    self.x = event.x
                    self.y = 700 - 1 - event.y
        elif self.set == True:
            self.attack = False
            for gets in game_world.enemy_objects():
                if gets.hp >= 0 and gets.x > 0:
                    if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < self.range:
                        self.attack = True
                        break
                else:
                    self.attack = False

            if self.attack == True:
                self.frame = (self.frame + 6 * game_framework.frame_time) % 3
                if self.attack_speed < get_time() - self.shottime:
                    fire = [poison_attack.fire(self.x, self.y, (3.141592/4) * i) for i in range(8) ]
                    for fires in fire :
                        game_world.add_object(fires, 0)
                    self.shottime = get_time()
            else:
                self.frame = (self.frame + 8 * game_framework.frame_time) % 4


    def draw(self):
        if self.attack == False:
            self.image.clip_composite_draw(0, 122 * int(self.frame ), 125, 122, self.radians, self.reflect, self.x, self.y,
                                           50, 50)
        else :
            self.image.clip_composite_draw(0, 488 + 122 * int(self.frame), 125, 122, self.radians, self.reflect, self.x, self.y,
                                           50, 50)


    def get_bb(self):
        return self.x, self.y, self.range
