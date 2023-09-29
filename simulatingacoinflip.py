import random

"""
this program simulates a coin flip by randomly generating one of two 
numbers that have an equal chance of being true and false. Each number
represents a side of the coin, heads or tails. It prints a random
coin flip for each time the program is run.
"""

coin = random.randint(1, 2)
if coin == 1:
    print("Heads")
else:
    print("Tails")