from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0

y = 0

z = 270

head = 1

   
if (head == 1):
    while (head < 4):
        clear_canvas_now()
        grass.draw_now(400, 30)
                        
        x = 220*math.cos(math.radians(z))
        y = 220*math.sin(math.radians(z))
        character.draw_now(x + 400 , y + 300)
                       

        z = z + 1
        delay(0.01)     
        


close_canvas()
