STARTING_ITEMS_IN_INVENTORY = 20

num_items = STARTING_ITEMS_IN_INVENTORY
# Enter your code here

num_buy = 0

while num_items > 0:
    print("We have " + str(num_items) + " items in inventory.")
    num_buy = int(input("How many would you like to buy? "))
    if num_buy == num_items:
        print("All out!")
        num_items = 0
    elif num_buy > num_items:
        print("There is not enough in inventory for that purchase.")
    else:
        num_items -= num_buy
        print("Now we have " + str(num_items) + " left")