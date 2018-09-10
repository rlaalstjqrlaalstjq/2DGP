from pico2d import *

import math

os.chdir('C:\\Users\김민섭\\Desktop\\2D 프로그래밍\\2018-2DGP\\Labs\\Lecture03')

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x= 0
y=0
i=0
angle=5
a= (math.radians(angle))

while True:
        while( x <800):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,90)
                x = x+4
                delay(0.01)
        while( y <570):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(790,y+90)
                y = y+4
                delay(0.01)
        while( x >0):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,560)
                x = x-4
                delay(0.01)   
        while( y > 0):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(0,y+90)
                y = y-4
                delay(0.01)
        while( x <400):
                clear_canvas_now()
                grass.draw_now(400,30)
                character.draw_now(x,90)
                x = x+4
                delay(0.01)
        for k in range(0,71):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x= 400 +210*(math.cos(a*(120-k)))
            y= 300 + 210*(math.sin(a*(120-k)))
            
            delay(0.04)
    
    
    

        
close_canvas()



    

