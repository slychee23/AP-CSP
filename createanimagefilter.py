# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
IMAGE_WIDTH = 420
IMAGE_HEIGHT = 300
IMAGE_LOAD_TIME = 1000

image = Image(IMAGE_URL)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)

"""
 Filter that takes an image as a parameter
 and applies a filter, then returns the filtered image
"""
# This is an example of an invert filter
def custom_pixel(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    pixel[0] = 200 - red
    pixel[1] = 200 - green
    pixel[2] = 255 - blue
    return (pixel[0], pixel[1], pixel[2])
    
def custom_filter(image):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            custom_pix = custom_pixel(pixel)
            image.set_red(x, y, custom_pix[0])
            image.set_green(x, y, custom_pix[1])
            image.set_blue(x, y, custom_pix[2])
    return image

def change_image():
    global image
    image = custom_filter(image)
    
    
timer.set_timeout(change_image, IMAGE_LOAD_TIME)