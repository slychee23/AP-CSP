width = get_width()
height = get_height()

# Create a Blue rectangle on left
blue_rect = Rectangle(width/3, height)
blue_rect.set_color(Color.blue)
blue_rect.set_position(0,0)
add(blue_rect)

# Create a Red rectangle on right
red_rect = Rectangle(width/3, height)
red_rect.set_color(Color.red)
red_rect.set_position(width - width/3, 0)
add(red_rect)