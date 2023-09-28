import random

# Enter your code here

num_rolled = 0

while True: 
    num_rolled += 1
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print("Rolled: " + str(roll1) + " " + str(roll2))
    if roll1 == 1 and roll2 == 1:
        print("It took you " + str(num_rolled) + " rolls to get snake eyes.")
        break