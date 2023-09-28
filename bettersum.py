# Enter your code here

num1 = int(input("Enter one number: "))
num2 = int(input("Enter second number: "))

sum = 0
for i in range(num1, num2 + 1):
	sum += i

print("The sum is " + str(sum))