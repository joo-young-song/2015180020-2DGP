from pico2d import *

open_canvas(800, 600)

grass = None

enemy_tile = None

class Grass:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.image = load_image('grass1.jpg')

    def draw(self):
        self.image.draw(0, 0, 100, 100)


grass = Grass()





while True:

    clear_canvas()

    grass.draw()

    update_canvas()