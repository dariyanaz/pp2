def rev_list(list):
    new_list = []
    reversed_list = reversed(list)
    for num in reversed_list:
        new_list.append(num)
        
    return new_list
        
list_num = [1, 2, 3, 4, 5]
print(rev_list(list_num))