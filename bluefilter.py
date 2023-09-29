# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)

#################################################
# Write your function here. Loop through each pixel
# and set each pixel to have a zero blue value.
#################################################
def remove_blue():
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            pixel = image.get_pixel(x,y)
            image.set_blue(x, y, 0)
# Give the image time to load
print("Removing Blue Channel ....")
print("Might take a minute....")
timer.set_timeout(remove_blue, 1000)