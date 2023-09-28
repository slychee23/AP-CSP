# Start coding here. Don't forget to click the canvas
# before you try to use the arrow keys!

def circle_size(event):
    if event.key == "ArrowLeft":
        circle.set_radius(circle.get_radius() - 10)
    if event.key == "ArrowRight":
        circle.set_radius(circle.get_radius() + 10)
        
circle = Circle(100)
circle.set_position(250, 250)
circle.set_color(Color.purple)
add(circle)

add_key_down_handler(circle_size)