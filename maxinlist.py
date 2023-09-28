def max_int_in_list(my_list):
    biggest = my_list[-1]
    for num in my_list:
        if num > biggest:
            biggest = num
    return biggest