# This program should draw a stop light

LIGHT_RADIUS = 25
STOPLIGHT_WIDTH = 100
STOPLIGHT_HEIGHT = 250
BUFFER = 75

# Implement a function that draws a single circle 
# with radius LIGHT_RADIUS.
# The circle should be in the center of the screen horizontally.
# Use the parameters for the y position and color


def draw_circle(color, y):
    circ = Circle(LIGHT_RADIUS)
    circ.set_color(color)
    circ.set_position(x, y)
    add(circ)

def draw_rectangle():
    rect = Rectangle(STOPLIGHT_WIDTH, STOPLIGHT_HEIGHT)
    rect.set_color(Color.gray)
    rect.set_position(x - STOPLIGHT_WIDTH/2, y - STOPLIGHT_HEIGHT/2)
    add(rect)


y = get_height()/2
x = get_width()/2

draw_rectangle()
draw_circle(Color.red, y - BUFFER)
draw_circle(Color.yellow, y)
draw_circle(Color.green, y + BUFFER)