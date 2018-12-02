from pico2d import *

tile_rotate = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 12, 12, 12, 12],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 12, 12, 12, 12],
               [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 12, 12, 12, 12],
               [2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 12, 12, 12, 12],
               [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 13, 14, 14],
               [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 13, 14, 14],
               [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 11, 11],
               [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 11, 11],
               [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 8, 9, 9],
               [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 8, 8, 9, 9],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 7, 7, 7, 7],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 7, 7, 7, 7],
               [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 7, 7, 7, 7],
               [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 7, 7, 7, 7]
               ]


class Grass:
    def __init__(self):
        self.image = load_image('background_image//grass 1.jpg')
        self.bgm = load_music('sound//stage2.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


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

class Ui_Back:
    def __init__(self):
        self.back = load_image('background_image//wood_ui.png') # 140 140 900 550
        pass
    def update(self):
        pass

    def draw(self):
        self.back.draw(900, 350)

class Ui_Tower:
    def __init__(self):
        self.poison_tower = load_image('tower_image//poison_tower_UI.png') # 875 ,450
        self.ice_tower = load_image('tower_image//ice_tower_UI.png') # 925, 450
    def update(self):
        pass
    def draw(self):
        font = load_font('ENCR10B.TTF', 20)
        self.poison_tower.draw(850, 450, 100, 100)
        font.draw(875, 475, '25' , (255, 255, 255))
        self.ice_tower.draw(950, 450, 100, 100)
        font.draw(975, 475, '50', (255, 255, 255))

class Ui_Button:
    def __init__(self):
        self.undo_button = load_image('background_image//undo.png') # 140 140 900 550
        #self.undo_button_2 = load_image('background_image//undo2.png') # 140 140
        self.money_image = load_image('background_image//money.png') # 400 400 850 500
        self.egg_image = load_image('background_image//eggs.png')
        self.point_image = load_image('background_image//point.png')
        pass

    def update(self):
        pass

    def draw(self):
        self.undo_button.draw(900, 100)
        self.money_image.draw(850, 650)
        self.egg_image.draw(850, 550, 100, 100)
        self.point_image.draw(50,650,30,30)
        #self.point_image.draw(750, 50, 30, 30)
        self.point_image.clip_composite_draw(0, 0, 61, 106, -3.141592/2, '', 750, 50,  30,  30)
