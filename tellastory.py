#This program tells a story between a mouse and a bird. 
x = get_width()
y = get_height()
center_x = get_width()/2
center_y = get_height()/2
    
def draw_background():
    sky = Rectangle(x, y)
    sky.set_position(0, 0)
    sky.set_color(Color.blue)
    add(sky)
    
    grass = Rectangle(x, center_y)
    grass.set_position(0, center_y + 40)
    grass.set_color(Color.green)
    add(grass)
    
    tree = Rectangle(60, y)
    tree.set_position(0, 70)
    tree.set_color(Color.brown)
    add(tree)
    
    branch = Rectangle(110, 20)
    branch.set_position(0, center_y - 40)
    branch.set_color(Color.brown)
    add(branch)
    
    treetop = Rectangle(120, 70)
    treetop.set_position(0, 0)
    treetop.set_color(Color.green)
    add(treetop)
    
    treetop2 = Rectangle(140, 40)
    treetop2.set_position(0, 0)
    treetop2.set_color(Color.green)
    add(treetop2)
    
def draw_circle(x, y, color, radius):
    eyes = Circle(radius)
    eyes.set_position(x, y)
    eyes.set_color(color)
    add(eyes)
    
def add_dialogue(label, x, y):
    txt = Text(label)
    txt.set_position(x, y)
    txt.set_color(Color.black)
    txt.set_font("12pt Arial")
    add(txt)
    
def draw_mouse():
    body = Rectangle(70, 30)
    body.set_position(center_x, center_y + 80)
    body.set_color(Color.gray)
    add(body)
    
    draw_circle(center_x, center_y + 80, Color.gray, 20) #head
    draw_circle(center_x - 20, center_y + 80, Color.red, 3) #nose
    draw_circle(center_x, center_y + 70, Color.black, 3) #eye
    
    draw_circle(center_x + 5, center_y + 110, Color.gray, 7)   #legs
    draw_circle(center_x + 20, center_y + 110, Color.gray, 7)
    draw_circle(center_x + 45, center_y + 110, Color.gray, 7)
    draw_circle(center_x + 60, center_y + 110, Color.gray, 7)
    
    draw_circle(center_x - 10, center_y + 60, Color.gray, 10) #ears
    draw_circle(center_x + 15, center_y + 60, Color.gray, 10)
    
    tail = Line(center_x + 70, center_y + 90, center_x + 100, center_y + 100)
    tail.set_color(Color.red)
    add(tail)
    
def draw_flipped_mouse():
    body = Rectangle(70, 30)
    body.set_position(center_x - 30, center_y + 70)
    body.set_color(Color.gray)
    add(body)
    
    draw_circle(center_x + 40, center_y + 70, Color.gray, 20) #head
    draw_circle(center_x + 60, center_y + 70, Color.red, 3) #nose
    draw_circle(center_x + 40, center_y + 60, Color.black, 3) #eye
    
    draw_circle(center_x - 40, center_y + 100, Color.gray, 7)   #legs
    draw_circle(center_x - 10, center_y + 110, Color.gray, 7)
    draw_circle(center_x + 20, center_y + 110, Color.gray, 7)
    draw_circle(center_x + 50, center_y + 105, Color.gray, 7)
    
    draw_circle(center_x + 30, center_y + 50, Color.gray, 10) #ears
    draw_circle(center_x + 50, center_y + 50, Color.gray, 10)
    
    tail = Line(center_x - 30, center_y + 75, center_x - 60, center_y + 60)
    tail.set_color(Color.red)
    add(tail) 
    
def draw_bird(): 
    draw_circle(85, center_y - 50, Color.black, 20) #body
    draw_circle(100, center_y - 60, Color.black, 15) #head
    draw_circle(100, center_y - 60, Color.white, 3) #eye
    add_dialogue(">", 115, 190) #beak

def draw_bear():
    draw_circle(550, center_y - 40, Color.brown, 250) #body
    draw_circle(350, -50, Color.brown, 100) #head
    draw_circle(400, 400, Color.brown, 30) #leg
    draw_circle(280, -20, Color.orange, 30) #snout
    
    mouth = Line(280, 20, 300, 20)
    mouth.set_color(Color.black)
    add(mouth)
    
    arm = Line(350, center_y - 70, 370, center_y) 
    arm.set_color(Color.black)
    add(arm)
    arm2 = Line(370, center_y, 400, center_y + 20)
    arm2.set_color(Color.black)
    add(arm2)

def draw_scene1():
    draw_background()
    draw_mouse()
    draw_bird()
    leaf = Line(center_x + 30, center_y + 90, center_x + 40, center_y + 85)
    leaf.set_color(Color.brown)
    add(leaf)
    add_dialogue("Hello! I'm up here!", 70, 150)
    add_dialogue("Ah, hi.", center_x - 30, center_y + 20)

def draw_scene2():
    draw_background()
    draw_mouse()
    draw_bird()
    add_dialogue("Oh, thank you!", center_x - 30, center_y + 20)
    add_dialogue("Just wanted to let you know you have a ", 30, 130)
    add_dialogue("branch stuck on your back.", 30, 150)

def draw_scene3():
    draw_background()
    draw_mouse()
    draw_bird()
    draw_bear()
    add_dialogue("Also, there's a bear behind you.", 20, 140)

def draw_scene4():
    draw_background()
    draw_flipped_mouse()
    draw_bird()
    draw_bear()
    smile = Line(300, 20, 290, 30)
    smile.set_color(Color.black)
    add(smile)
    add_dialogue("AHHHHH!", center_x - 30, center_y + 20)
    add_dialogue("Hello there.", 200, 40)

"""
 This is set up code that makes the story advance from
 scene to scene. Feel free to check out this code and
 learn how it works!
 But be careful! If you modify this code the story might
 not work anymore.
"""
scene_counter = 0

# When this function is called the next scene is drawn.

def draw_next_screen(x, y):
    global scene_counter
    scene_counter += 1

    if scene_counter == 1:
        draw_scene1()
    elif scene_counter == 2:
        draw_scene2()
    elif scene_counter == 3:
        draw_scene3()
    else:
        draw_scene4()

welcome = Text("Click to Begin!")
welcome.set_position(get_width() / 2 - welcome.get_width() / 2, get_height() / 2)
add(welcome)

add_mouse_click_handler(draw_next_screen)