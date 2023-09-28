SENTINEL = 0

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

x = 1

while x != SENTINEL:
    x = int(input("Enter a number: "))
    if is_even(x) == True:
        print("Even")
    else:
        print("Odd")

print("Done!")