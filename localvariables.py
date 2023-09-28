# All you have to do in this exercise is write a good comment that explains
# what local variables are. You should also give an example of a function
# and what the local variables are, and what the scope is of the variable.

#local variables are defined and can only be accessed within the function. 
#After execution, the local variable is discarded.

def square(y):  # function squares value y
    result = y * y
    return result 

"""the local variables are "y" and "result". Their scope is within the 
square(y) function, and therefore the local variables are only accessible
within that function. """