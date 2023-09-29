lastname_list = []
for i in range(5):
    name = input("Name: ")
    lastname_list.append(name.split()[-1])

lastname_list.sort()
print(lastname_list)