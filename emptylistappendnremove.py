# Enter your code here

list = []
list.append(3)
list.append("hello")
list.append(False)

for i in range(len(list)):
    print(list[i])

list.remove(3)
list.remove(False)
print(list)