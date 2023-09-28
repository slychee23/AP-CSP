# Enter your code here

def minVal(x, y):
    if x > y:
        return y
    else:
        return x

x = minVal(10, 14)
print("The min is " + str(x))

x = minVal(23, 88)
print("The min is " + str(x))