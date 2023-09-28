# Enter your code here

n = int(input("Enter value for N: "))
result = 1

for i in range(1, n + 1):
    result *= i
    print(result)