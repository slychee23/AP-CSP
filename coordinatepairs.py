import math

# fill in this function to return the distance between the two points!
def distance(first_point, second_point):
    x1 = first_point[0]
    y1 = first_point[1]
    x2 = second_point[0]
    y2 = second_point[1]
    x_pwr = pow(x2 - x1, 2)
    y_pwr = pow(y2 - y1, 2)
    sum_num = x_pwr + y_pwr
    return math.sqrt(sum_num)