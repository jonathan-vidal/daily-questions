def even_odd_list(num_list):
    return [num for num in num_list if num % 2 == 0] + [num for num in num_list if num % 2 != 0]