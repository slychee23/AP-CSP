"""
 Write a program that guesses every possible 4 digit passcode
 combinations until the correct passcode is guessed.

 The passcode is randomly generated and stored in the variable
 secretPasscode.

 Print out how many guesses it took to guess the correct passcode.
"""
import random

# Checks whether the given guess passcode is the correct passcode
def is_correct(guess_code, correct_code):
    return guess_code == correct_code

# Generates a random 4 digit passcode and returns it as a String
def generate_random_passcode():
    random_passcode = ""
    
    for i in range(4):
        random_digit = random.randint(0, 9)
        random_passcode += str(random_digit)
    return random_passcode

secret_passcode = generate_random_passcode()

# Write your code here

for i in range(10):
    guess_code = int(input("Enter Passcode (4 digits): "))
    correct_code = ""
    if is_correct(guess_code, correct_code):
        print("Correct passcode!")
        break
    else:
        print("Wrong passcode. Please try again. ")

print("It took " + str(i) + " guesses.")