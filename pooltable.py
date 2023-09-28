POOL_BALL_RADIUS = 40
FONT_TYPE = "30pt Arial"


# Write your function here that draws a pool ball. (Make sure to use the correct name)
# Find the center to use for the ball and number
x = get_width() / 2
y = get_height() / 2

def draw_pool_ball(color, number, x, y):
    ball = Circle(POOL_BALL_RADIUS)
    ball.set_position(x, y)
    ball.set_color(color)
    add(ball)
    number = Text(number)
    number.set_color(Color.white)
    number.set_font(FONT_TYPE)
    number.set_position(x - number.get_width()/2, y + number.get_height()/2)
    add(number)

draw_pool_ball(Color.orange, 5, 100, 100)
draw_pool_ball(Color.red, 3, 150, 350)
draw_pool_ball(Color.blue, 2, 250, 140)
draw_pool_ball(Color.green, 6, 50, 200)