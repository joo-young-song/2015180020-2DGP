import game_framework
from pico2d import *
import choice_state


name = "TitleState"
image = None
bgm = None
def enter():
    global image
    global bgm
    bgm = load_music('sound//die.mp3')
    bgm.set_volume(85)
    bgm.play()
    image = load_image('background_image//game_over.jpg')

def exit():
    global image
    del (image)


def handle_events():
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                    game_framework.change_state(choice_state)


def draw():
    clear_canvas()
    image.draw(500, 350)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






