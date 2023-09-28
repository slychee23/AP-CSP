import random

RECT_HEIGHT = 50
RECT_WIDTH = 30

COLORS = (Color.red, Color.orange, Color.yellow, 
          Color.green, Color.blue, Color.black)
          

def draw_rect(x, y):
    color = random.choice(COLORS) 
    rect = Rectangle(RECT_WIDTH, RECT_HEIGHT)
    rect.set_color(color)
    rect.set_position(x - RECT_WIDTH/2, y - RECT_HEIGHT/2)
    add(rect)

add_mouse_click_handler(draw_rect)