def exclamation(text):
    my_list = list(text)
    for i in range(len(my_list)):
        if my_list[i] == 'i':
            my_list[i] = "!"
    return ''.join(my_list)