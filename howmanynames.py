
num_names = int(input("Number of names: "))
name_list = []

for i in range(num_names):
    name = input("Name: ")
    name_list.append(name)
    
print("First name: " + name_list[0])
print("Middle names: " + str(name_list[1:-1]))
print("Last name: " + name_list[-1])