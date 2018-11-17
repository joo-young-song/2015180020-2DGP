from pico2d import *

class set:
    image = None

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.radians = 0
        self.reflect = ''
        if set.image is None:
            set.image = load_image('tower_image//white_tower.png')

    def update(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                self.x = event.x
                self.y = 600 - 1 - event.y


    def draw(self):
        self.image.clip_composite_draw(0, 0, 100, 100, self.radians, self.reflect, self.x, self.y, 100, 100)



