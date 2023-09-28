SECRET = "abc123"
# Enter your code here

while True:
    password = input("Enter password: ")
    if password == SECRET:
        print("You got it!")
        break
    print("Sorry, that did not match. Please try again.")