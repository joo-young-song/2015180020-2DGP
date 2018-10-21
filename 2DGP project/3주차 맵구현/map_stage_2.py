from pico2d import *


tile_rotate = [   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

open_canvas(800, 600)

grass = None

enemy_tile = None

class Grass:
    def __init__(self):
        self.image = load_image('grass1.jpg')
    def draw(self):
        for x in range(16):
            for y in range(12):
                if tile_rotate[y][x] == 0 :
                    self.image.draw(x * 50 + 25, y * 50 + 25, 50, 50)

class Tile:
    def __init__(self):
        self.image = load_image('tile1.jpg')
    def draw(self):
        for x in range(16):
            for y in range(12):
                if tile_rotate[y][x] == 1 :
                    self.image.rotate_draw(0, x * 50 + 25, y * 50 + 25, 50, 50)
                if tile_rotate[y][x] == 2:
                    self.image.rotate_draw(1.57, x * 50 + 25, y * 50 + 25, 50, 50)



grass = Grass()

enemy_tile = Tile()


while True:

    clear_canvas()

    grass.draw()

    enemy_tile.draw()

    update_canvas()