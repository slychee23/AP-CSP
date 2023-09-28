import random

set_size(480, 400)
SIDE_LENGTH = 100

# This graphics program should draw a square. 
# The fill color should be randomly choosen from
# the COLORS list

COLORS = [Color.red, Color.orange, Color.yellow, Color.green, Color.blue, 
        Color.purple, Color.black, Color.gray]

x = 480 / 2
y = 400 / 2

color = random.choice(COLORS) 
rect = Rectangle(SIDE_LENGTH, SIDE_LENGTH)
rect.set_color(color)
rect.set_position(x - SIDE_LENGTH / 2, y - SIDE_LENGTH / 2)
add(rect)