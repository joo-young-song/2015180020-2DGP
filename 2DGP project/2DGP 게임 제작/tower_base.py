from pico2d import *
import game_world
import math
import tower_attack

class tower:
    image = None

    def __init__(self, x = 0, y = 0, set = False):
        self.x = x
        self.y = y
        self.radians = 0.0
        self.frame = 0
        self.attack_speed = 0
        self.reflect = ''
        self.attack = False
        self.set = set
        self.range = 300
        if tower.image is None:
            tower.image = load_image('white_tower.png')

    def update(self):
        if self.set == False:
            events = get_events()
            for event in events:
                if event.type == SDL_MOUSEMOTION:
                    self.x = event.x
                    self.y = 600 - 1 - event.y
        elif self.set == True:

            if self.attack_speed > 0:
                self.attack_speed -= 1

            if self.attack == False:
                self.frame = (self.frame + 1) % 4
            else:
                self.frame = (self.frame + 1) % 2
                if self.frame == 1:
                    self.attack = False
                    self.attack_speed = 10

            for enemy_object in game_world.enemy_objects():
                if math.sqrt((self.x - enemy_object.x) * (self.y - enemy_object.y) + (self.y - enemy_object.y) * (
                        self.y - enemy_object.y) < self.range):
                    self.attack = True
                    self.frame = 1
                    tower_attack.fire(self.x, self.y, self.radians)

    def draw(self):
        if self.attack == False:
            self.image.clip_composite_draw(0, 100 + 100 * self.frame, 100, 100, self.radians, self.reflect, self.x, self.y, 100, 100)

        else :
            self.image.clip_composite_draw(0, 100 + 100 * (self.frame + 4), 100, 100, self.radians, self.reflect, self.x, self.y, 100, 100)


