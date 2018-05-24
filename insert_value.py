def insert_val_at(index, my_list, value):
    if (index >= len(my_list)):
        return False
    length = len(my_list) - 1
    my_list.append(my_list[length])
    for i in range(length, index, -1):
        my_list[i] = my_list[i-1]
    my_list[index] = value
    return my_list