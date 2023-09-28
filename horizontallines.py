# Write a function to draw a horizontal
# line given a y position and a length

def horizontal_line(x2, y2):
    line = Line(0, y2, x2, y2)
    line.set_position(0, y2)
    line.set_endpoint(x2, y2)
    add(line)

horizontal_line(100, 200)
horizontal_line(200, 100)
horizontal_line(300, 20)