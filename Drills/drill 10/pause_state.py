import pico2d
import game_framework
import main_state
name = "PauseState"

pause_screen = None


class Pause:
    def __init__(self):
        self.image = pico2d.load_image('pause.png')
        self.frame = 0

    def draw(self):
        if self.frame % 30 > 10:
            self.image.draw(400, 300)

    def update(self):
        self.frame += 1
        pico2d.delay(0.01)


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
    events = pico2d.get_events()

    for event in events:

        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()

        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_p:
            game_framework.pop_state()


def update():
    pause_screen.update()


def draw():
    pico2d.clear_canvas()

    pause_screen.draw()

    pico2d.update_canvas()
