from pico2d import *
import game_world
import math
import green_attack
import game_framework
import stage_1



class tower_g:
    image = None

    def __init__(self, x=0, y=0, set=False):
        self.x = x
        self.y = y
        self.radians = 0.0
        self.frame = 1
        self.attack_speed = 5
        self.lazer_attack_rate = 0
        self.reflect = ''
        self.attack = False
        self.set = set
        self.range = 500
        self.shottime = get_time()
        self.lazer_list = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
        if tower_g.image is None:
            tower_g.image = load_image('tower_image//green_tower.png')

    def update(self):
        self.frame = (self.frame + 6*game_framework.frame_time) % 3
        if self.set == False:
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
                        self.radians = math.atan2((gets.y - self.y),(gets.x - self.x))
                        self.attack = True
                        break


            if self.attack == True:
                if self.attack_speed < get_time() - self.shottime:
                    get_attack = [green_attack.fire(self.x, self.y, self.radians,self.lazer_list[i], i/16) for i in range(20)]
                    for fire in get_attack :
                        game_world.add_object(fire, 1)
                    self.shottime = get_time()

    def draw(self):
        if self.attack == False:
            self.image.clip_composite_draw(0, 50 * int(self.frame), 50, 50, self.radians, self.reflect, self.x, self.y,
                                           50, 50)

        else:
            self.image.clip_composite_draw(0, 0, 50, 50, self.radians, self.reflect, self.x,
                                           self.y, 50, 50)

    def get_bb(self):
        return self.x, self.y, self.range