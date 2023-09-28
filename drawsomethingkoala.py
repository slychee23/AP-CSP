# Make your creation here!
# Making a koala character

y = get_height()/2
x = get_width()/2

head = Circle(100)
head.set_position(x, y)
head.set_color(Color.gray)
add(head)

eye1 = Rectangle(30, 20)
eye1.set_position(x + 30, y - 20)
eye1.set_color(Color.white)
add(eye1)

eye2 = Rectangle(30, 20)
eye2.set_position(x - 60, y - 20)
eye2.set_color(Color.white)
add(eye2)

ear1 = Circle(50)
ear1.set_position(x - 80, y - 80)
ear1.set_color(Color.gray)
add(ear1)

ear2 = Circle(50)
ear2.set_position(x + 80, y - 80)
ear2.set_color(Color.gray)
add(ear2)

snout = Circle(30)
snout.set_position(x, y + 20)
snout.set_color(Color.white)
add(snout)

mouth = Line(x - 30, y + 50, x + 30, y + 50)
mouth.set_color(Color.black)
add(mouth)