import simplegui
import random

interval = 100
count = 0
total_stops = 0
succes_stops = 0
stop = True
a = 0
b = 0
c = 0
d = 0

def start():
    timer.start()

def stop():
    global succes_stops, total_stops  
    total_stops = total_stops + 1
    if d==0:
        succes_stops = succes_stops + 1 
    timer.stop()

def draw_handler(canvas):
    canvas.draw_text(str(a), (115, 150), 50,  'White')
    canvas.draw_text(":", (145, 150), 60, 'White')
    canvas.draw_text(str(b), (160, 150), 50,  'White')
    canvas.draw_text(str(c), (190, 150), 50,  'White')
    canvas.draw_text(".", (210, 150), 50, 'White')
    canvas.draw_text(str(d), (225, 150), 50,  'White')
    canvas.draw_text(str(succes_stops), (300, 50), 50,  'Red')
    canvas.draw_text("/", (325, 50), 50,  'Red')
    canvas.draw_text(str(total_stops), (340, 50), 50,   'Red')

def reset():
    global a, b, c, d, succes_stops, total_stops
    a = 0
    b = 0
    c = 0
    d = 0
    succes_stops = 0
    total_stops = 0

def timer_handler():  
    global a,b,c,d
    d = d + 1
    if d == 10:
        d = 0
        global c
        c = c + 1
        if c == 10:
            c = 0
            global b
            if b == 6:
                b = 0
                global a
                a = a + 1

             
frame = simplegui.create_frame('Testing', 390, 300)
frame.set_canvas_background('Blue')
button1 = frame.add_button('start', start, 100,)
button2 = frame.add_button('stop', stop, 100)
button3 = frame.add_button('restart', reset,100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, timer_handler)
frame.start()                
   