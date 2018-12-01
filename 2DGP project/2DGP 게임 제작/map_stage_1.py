from pico2d import *


tile_rotate = [[0, 0, 0, 3, 3, 3, 3, 3, 4, 0, 0, 3, 3, 3, 3, 5, 12, 12, 12, 12],
               [0, 0, 0, 2, 2, 3, 3, 3, 4, 0, 0, 2, 2, 3, 3, 5, 12, 12, 12, 12],
               [0, 0, 0, 2, 2, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 12, 12, 12, 12],
               [0, 0, 0, 2, 2, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 12, 12, 12, 12],
               [0, 0, 0, 2, 2, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 13, 13, 14, 14],
               [3, 3, 3, 3, 2, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 13, 13, 14, 14],
               [3, 3, 3, 3, 2, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 10, 10, 11, 11],
               [0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 10, 10, 11, 11],
               [0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 8, 8, 9, 9],
               [0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 8, 8, 9, 9],
               [0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 7, 7, 7, 7],
               [0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 0, 7, 7, 7, 7],
               [0, 0, 0, 0, 0, 0, 0, 4, 4, 3, 3, 3, 2, 0, 0, 0, 7, 7, 7, 7],
               [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 2, 0, 0, 0, 7, 7, 7, 7]
               ]


class Grass:
    def __init__(self):
        self.image = load_image('background_image//grass 1.jpg')

    def update(self):
        pass

    def draw(self):
        for x in range(16):
            for y in range(14):
                if tile_rotate[y][x] == 0:
                    self.image.draw(x * 50 + 25, y * 50 + 25, 50, 50)


class Tile:
    def __init__(self):
        self.image = load_image('background_image//tile 1.jpg')

    def update(self):
        pass

    def draw(self):
        for x in range(16):
            for y in range(14):
                if tile_rotate[y][x] != 0:
                    self.image.rotate_draw(0, x * 50 + 25, y * 50 + 25, 50, 50)


class Ui_Tower:
    def __init__(self):
        self.white_tower = load_image('tower_image//white_tower_UI.png') # 875 ,450
        self.red_tower = load_image('tower_image//red_tower_UI.png') # 925, 450
        self.green_tower = load_image('tower_image//green_tower_UI.png') # 875, 350
    def update(self):
        pass
    def draw(self):
        font = load_font('ENCR10B.TTF', 20)
        self.white_tower.draw(850, 450)
        font.draw(875, 475, '50' , (255, 255, 255))
        self.red_tower.draw(950, 450)
        font.draw(975, 475, '100', (255, 255, 255))
        self.green_tower.draw(850, 350)
        font.draw(875, 375, '150', (255, 255, 255))



class Ui_Button:
    def __init__(self):
        self.undo_button = load_image('background_image//undo.png') # 140 140 900 550
        #self.undo_button_2 = load_image('background_image//undo2.png') # 140 140
        self.money_image = load_image('background_image//money.png') # 400 400 850 500
        pass

    def update(self):
        pass

    def draw(self):
        self.undo_button.draw(900, 100)
        self.money_image.draw(850, 650)