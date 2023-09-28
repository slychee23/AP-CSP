# Constants representing the radius of the top, middle,
# and bottom snowball.
BOTTOM_RADIUS = 100
MID_RADIUS = 60
TOP_RADIUS = 30

width = get_width()
height = get_height()

#top circle
top_circ = Circle(TOP_RADIUS)
top_circ.set_color(Color.gray)
top_circ.set_position(width/2, height/3.5)
add(top_circ)

#mid circle
mid_circ = Circle(MID_RADIUS)
mid_circ.set_color(Color.gray)
mid_circ.set_position(width/2, height/2.15)
add(mid_circ)

#bottom circle
bot_circ = Circle(BOTTOM_RADIUS)
bot_circ.set_color(Color.gray)
bot_circ.set_position(width/2, height - BOTTOM_RADIUS)
add(bot_circ)