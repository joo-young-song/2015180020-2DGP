from pico2d import *
import game_world
import math
import green_attack
import stage_1



class tower_g:
    image = None

    def __init__(self, x=0, y=0, set=False):
        self.x = x
        self.y = y
        self.radians = 0.0
        self.frame = 1
        self.attack_speed = 150
        self.lazer_attack_rate = 0
        self.reflect = ''
        self.attack = False
        self.set = set
        self.range = 500
        self.lazer_list = {0, 1, 1, 1, 1, 1, 1, 1, 1, 2}
        if tower_g.image is None:
            tower_g.image = load_image('green_tower.png')

    def update(self):
        if self.set == False:
            events = get_events()
            for event in events:
                if event.type == SDL_MOUSEMOTION:
                    self.x = event.x
                    self.y = 600 - 1 - event.y
        elif self.set == True:
            for gets in stage_1.enemy_1:
                if gets.hp >= 0 and self.attack == False:
                    if math.sqrt((gets.x - self.x) * (gets.x - self.x) + (gets.y - self.y) * (gets.y - self.y)) < self.range:
                        self.radians = math.atan2((gets.y - self.y),(gets.x - self.x))
                        self.attack_speed -= 1
                        break

            if self.attack == False:
                self.frame = (self.frame + 1) % 3 + 1

                if self.attack_speed < 0:
                    self.attack = True

            elif self.attack == True:
                self.attack_speed -= 1
                if self.attack_speed < 0:

                    get_attack = green_attack.fire(self.x, self.y, self.radians,1)

                    game_world.add_object(get_attack, 2)

                    if self.attack_speed < -10:
                        self.attack_speed = 150

                        self.attack = False

    def draw(self):
        if self.attack == False:
            self.image.clip_composite_draw(0, 50 * self.frame, 50, 50, self.radians, self.reflect, self.x, self.y,
                                           50, 50)

        else:
            self.image.clip_composite_draw(0, 0, 50, 50, self.radians, self.reflect, self.x,
                                           self.y, 50, 50)

    def get_bb(self):
        return self.x, self.y, self.range