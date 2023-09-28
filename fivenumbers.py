num_list = []

for i in range(5):
    num = int(input("Number: "))
    num_list.append(num)
    print(num_list)

print("Sum: " + str(sum(num_list)))