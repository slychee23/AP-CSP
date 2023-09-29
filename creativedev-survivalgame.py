def story_begins():
    print("You have mysteriously woken up on the shore of a deserted island")
    print("You must survive until the next day when you will be rescued.")
    print("Choose the following options: ")
    
    choice = input("Would you like to catch fish or look for fruits? Enter 'fish' or 'fruit': ")
    
    if choice == 'fruit':
        choose_fruit()
    elif choice == 'fish':
        choose_fish()
    else:
        print("Invalid choice. Please choose again.")
        story_begins()

def choose_next():
    print("You now have the energy to increase your chance of survival!")
    print("Choose the following options: ")
    
    choice = input("Would you like to build a shelter or make a fire? Enter 'shelter' or 'fire': ")
    
    if choice == 'shelter':
        make_shelter()
    elif choice == 'fire':
        make_fire()
    else:
        print("Invalid choice. Please choose again.")
        choose_next()
        
def choose_next2():
    print("You don't have as much energy to increase your chance of survival.")
    print("Choose the following options: ")
    
    choice = input("Would you like to build a shelter or look for fruit on a tree? Enter 'shelter' or 'tree': ")
    
    if choice == 'shelter':
        make_shelter_fail()
    elif choice == 'tree':
        climb_tree()
        
def make_shelter_fail():
    print("You have attempted to make a shelter, however it collapsed in the middle of the night and you were eaten by a wild animal.")
    print("Better luck next time!")
    
def climb_tree():
    print("You have successfully climbed a tree and accidentally fell asleep on it before you could take the fruit")
    print("You woke up the next day safe and sound. Congratulations! You have survived!")
    
def choose_fruit():
    print("You have chosen to look for fruit. You scavenge around and in no time you find some fallen coconuts.")
    choose_next()
    
def choose_fish():
    print("You have chosen to catch fish. Due to your lacking skills, you were unable to catch any fish and are left hungry")
    choose_next2()
    

def make_fire():
    print("You decided to make a fire to keep warm and fend from dangerous animals.")
    print("Unfortunately, it began to rain, and the fire you had spent so much time on had been put out. Without shelter, you would be eaten by a wild animal ")
    print("You did not survive! Better luck next time!")
    
def make_shelter():
    print("You decided to make a shelter to protect you from animals.")
    print("The makeshift tent managed to survive the night and so did you!")
    print("Congratulations! You have survived!")
    
def hunt_food():
    print("You decide to hunt for food.")
    print("With your lacking hunting skills, you were unable to hunt for any food, leaving you with time wasted and a hungry stomach")
    
story_begins()