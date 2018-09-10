from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0

y = 0

head = 0
while(head < 5):
    if(head == 0):
        while (x < 800):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x + 2
            if(x >= 800):
                head = 1 
            delay(0.01)    
    elif(head == 1):
        while (y < 510):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(800, y + 90)
            y = y + 2
            if(y >= 510):
                head = 2
            delay(0.01)
    elif(head == 2):
        while (x > 0):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 600)
            x = x - 2
            if(x <= 0):
                head = 3
            delay(0.01)
           
    elif(head == 3):
        while (y > 0):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(0, y + 90)
            y = y - 2
            if(y <= 0):
                head = 0
            delay(0.01)
        
    


close_canvas()
