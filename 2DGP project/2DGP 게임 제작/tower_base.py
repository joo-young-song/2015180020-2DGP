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
        self.attack_speed = 100
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
            if self.attack == False:
                self.attack_speed -= 1
                self.frame = (self.frame + 1) % 4

                if self.attack_speed < 0:
                    self.attack = True

            elif self.attack == True:
                self.frame = (self.frame + 1) % 2


    def draw(self):
        if self.attack == False:
            self.image.clip_composite_draw(0, 100 * self.frame, 100, 100, self.radians, self.reflect, self.x, self.y, 100, 100)

        else :
            self.image.clip_composite_draw(0, 100 * (self.frame + 4), 100, 100, self.radians, self.reflect, self.x, self.y, 100, 100)


