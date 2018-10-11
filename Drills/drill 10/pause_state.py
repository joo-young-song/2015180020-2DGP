from pico2d import *

import game_framework

import main_state

name = "PauseState"

pause_screen = None


class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.frame = 0

    def draw(self):
        if self.frame % 30 > 10:
            self.image.draw(400, 300)

    def update(self):
        self.frame += 1
        delay(0.01)


def enter():
    global pause_screen

    pause_screen = Pause()


def exit():
    global pause_screen
    del pause_screen


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()

    for event in events:

        if event.type == SDL_QUIT:

            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.change_state(main_state)


def update():
    pause_screen.update()


def draw():
    clear_canvas()

    pause_screen.draw()

    update_canvas()
