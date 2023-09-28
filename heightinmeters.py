INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12

# Enter your code here

def convert_height_to_meters(feet, inches):
    INCHES = feet * FEET_TO_INCHES
    CM1 = INCHES * INCHES_TO_CM
    CM2 = inches * INCHES_TO_CM
    METERS = (CM1 + CM2)* CM_TO_METERS
    print(str(feet) + " feet, " + str(inches) + " inches = " + str(METERS) + " meters")
    
convert_height_to_meters(6, 8)
convert_height_to_meters(100, 90)
convert_height_to_meters(88, 23)