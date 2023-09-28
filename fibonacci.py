MAX = 1000
first = 1 # previous number 1
second = 1 # previous number 2
next_num = first + second

print(first)
print(second)

while next_num <= MAX:
    print(next_num)
    first, second = second, next_num
    next_num = first + second