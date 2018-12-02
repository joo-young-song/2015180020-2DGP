from pico2d import *


tile_rotate = [[3, 3, 5, 5, 5, 4, 0, 0, 0, 0, 3, 3, 5, 5, 5, 4, 12, 12, 12, 12],
               [5, 5, 5, 5, 5, 4, 0, 0, 0, 0, 5, 5, 5, 5, 5, 4, 12, 12, 12, 12],
               [5, 5, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5, 12, 12, 12, 12],
               [5, 5, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5, 12, 12, 12, 12],
               [2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 13, 13, 14, 14],
               [2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 13, 13, 14, 14],
               [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 10, 10, 11, 11],
               [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 10, 10, 11, 11],
               [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 8, 8, 9, 9],
               [3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 8, 8, 9, 9],
               [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5, 7, 7, 7, 7],
               [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5, 7, 7, 7, 7],
               [0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 2, 5, 5, 5, 5, 5, 7, 7, 7, 7],
               [0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 2, 5, 5, 5, 1, 1, 7, 7, 7, 7]
]

class Grass:
    def __init__(self):
        self.image = load_image('background_image//grass 1.jpg')

    def update(self):
        pass

    def draw(self):
        for x in range(16):
            for y in range(14):
                if tile_rotate[y][x] == 0 :
                    self.image.draw(x * 50 + 25, y * 50 + 25, 50, 50)

class Tile:
    def __init__(self):
        self.image = load_image('background_image//tile 1.jpg')
    def update(self):
        pass

    def draw(self):
        for x in range(16):
            for y in range(14):
                if tile_rotate[y][x] != 0 :
                    self.image.rotate_draw(0, x * 50 + 25, y * 50 + 25, 50, 50)

class Ui_Tower:
    def __init__(self):
        self.white_tower = load_image('tower_image//white_tower_UI.png') # 875 ,450
        self.red_tower = load_image('tower_image//red_tower_UI.png') # 925, 450
        self.green_tower = load_image('tower_image//green_tower_UI.png') # 875, 350
        self.poison_tower = load_image('tower_image//poison_tower_UI.png') # 875 ,450
        self.ice_tower = load_image('tower_image//ice_tower_UI.png') # 925, 450
    def update(self):
        pass
    def draw(self):
        font = load_font('ENCR10B.TTF', 20)
        self.white_tower.draw(850, 450)
        font.draw(875, 475, '50' , (255, 255, 255))
        self.red_tower.draw(950, 450)
        font.draw(960, 475, '100', (255, 255, 255))
        self.green_tower.draw(850, 350)
        font.draw(875, 375, '150', (255, 255, 255))

        self.poison_tower.draw(950, 350, 100, 100)
        font.draw(975, 375, '25' , (255, 255, 255))
        self.ice_tower.draw(850, 250, 100, 100)
        font.draw(875, 275, '50', (255, 255, 255))

class Ui_Back:
    def __init__(self):
        self.back = load_image('background_image//wood_ui.png') # 140 140 900 550
        pass
    def update(self):
        pass

    def draw(self):
        self.back.draw(900, 350)

class Ui_Button:
    def __init__(self):
        self.undo_button = load_image('background_image//undo.png') # 140 140 900 550
        self.money_image = load_image('background_image//money.png') # 400 400 850 500
        pass

    def update(self):
        pass

    def draw(self):
        self.undo_button.draw(900, 100)
        self.money_image.draw(850, 650)