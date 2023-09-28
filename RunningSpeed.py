# Enter your code here

miles = int(input("How many miles did you run? "))
minutes = int(input("How many minutes did it take you? "))
miles_per_hour = miles / (minutes / 60)

print("Speed in mph: " + str(miles_per_hour))