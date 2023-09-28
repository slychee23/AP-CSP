# Constants for body
HEAD_RADIUS = 35
BODY_WIDTH = HEAD_RADIUS * 2
BODY_HEIGHT = 60
NUM_FEET = 3
FOOT_RADIUS = (BODY_WIDTH) / (NUM_FEET * 2)

# Constants for eyes
PUPIL_RADIUS = 4
PUPIL_LEFT_OFFSET = 8
PUPIL_RIGHT_OFFSET = 20
EYE_RADIUS = 10
EYE_OFFSET = 14


# Put your function(s) here
def draw_ghost(center_x, center_y, color):
    head = Circle(HEAD_RADIUS)
    head.set_position(center_x, center_y)
    head.set_color(color)
    add(head)
    
    body = Rectangle(BODY_WIDTH, BODY_HEIGHT)
    body.set_position(center_x - HEAD_RADIUS, center_y)
    body.set_color(color)
    add(body)
    
    foot = Circle(FOOT_RADIUS)
    foot.set_position(center_x - BODY_WIDTH/3, center_y + BODY_HEIGHT)
    foot.set_color(color)
    add(foot)

    foot2 = Circle(FOOT_RADIUS)
    foot2.set_position(center_x, center_y + BODY_HEIGHT)
    foot2.set_color(color)
    add(foot2)
    
    foot3 = Circle(FOOT_RADIUS)
    foot3.set_position(center_x + BODY_WIDTH/3, center_y + BODY_HEIGHT)
    foot3.set_color(color)
    add(foot3)
    
    eye = Circle(EYE_RADIUS)
    eye.set_position(center_x - EYE_OFFSET, center_y)
    eye.set_color(Color.white)
    add(eye)
    
    eye2 = Circle(EYE_RADIUS)
    eye2.set_position(center_x + EYE_OFFSET, center_y)
    eye2.set_color(Color.white)
    add(eye2)
    
    pupil = Circle(PUPIL_RADIUS)
    pupil.set_position(center_x - PUPIL_LEFT_OFFSET, center_y)
    pupil.set_color(Color.blue)
    add(pupil)
    
    pupil2 = Circle(PUPIL_RADIUS)
    pupil2.set_position(center_x + PUPIL_RIGHT_OFFSET, center_y)
    pupil2.set_color(Color.blue)
    add(pupil2)   
    
center_x = get_width()/2
center_y = get_height()/2
draw_ghost(center_x, center_y, Color.red)
draw_ghost(100, 100, Color.green)
draw_ghost(370, 150, Color.black)
draw_ghost(40, 200, Color.orange)
draw_ghost(300, 50, Color.yellow)