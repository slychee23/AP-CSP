import random
# Enter your code here

MIN = 1
MAX = 100

random_num = random.randint(MIN, MAX)
x = 0
    
while x != random_num:
    x = int(input("Guess? "))
    if x < random_num:
        print("Low")
    elif x > random_num:
        print("High")
    else:
        print("Correct!")
        break