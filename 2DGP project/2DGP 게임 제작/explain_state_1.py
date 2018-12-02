import game_framework
from pico2d import *
import choice_state


name = "TitleState"
image = None
image2 = None
image3 = None
image4 = None

images = None
count = 0

def enter():
    global image
    global image2
    global image3
    global image4
    global images

    image = load_image('background_image//explain (1).png')
    image2 = load_image('background_image//explain (2).png')
    image3 = load_image('background_image//explain (3).png')
    image4 = load_image('background_image//explain (4).png')

    images = [image,image2,image3,image4]


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
                count += 1
                if count > 3 :
                    game_framework.change_state(choice_state)


def draw():
    global count
    global images
    clear_canvas()
    images[count].draw(500, 350, 1000, 700)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






