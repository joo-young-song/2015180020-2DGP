from pico2d import *


tile_rotate = [[3, 3, 5, 5, 5, 4, 0, 0, 0, 0, 3, 3, 5, 5, 5, 4],
               [5, 5, 5, 5, 5, 4, 0, 0, 0, 0, 5, 5, 5, 5, 5, 4],
               [5, 5, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5],
               [5, 5, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5],
               [2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
               [2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1],
               [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4],
               [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4],
               [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5],
               [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5],
               [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 2, 5, 5, 5, 5, 5],
               [0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 2, 5, 5, 5, 1, 1],
]

class Grass:
    def __init__(self):
        self.image = load_image('grass 1.jpg')

    def update(self):
        pass

    def draw(self):
        for x in range(16):
            for y in range(12):
                if tile_rotate[y][x] == 0 :
                    self.image.draw(x * 50 + 25, y * 50 + 25, 50, 50)

class Tile:
    def __init__(self):
        self.image = load_image('tile 1.jpg')
    def update(self):
        pass

    def draw(self):
        for x in range(16):
            for y in range(12):
                if tile_rotate[y][x] != 0 :
                    self.image.rotate_draw(0, x * 50 + 25, y * 50 + 25, 50, 50)