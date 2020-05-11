def my_max(num_list):
    curr_max = float('-inf')
    for num in num_list:
        if num > curr_max:
            curr_max = num

    return curr_max