def is_happy(num_to_check):
    curr_num = num_to_check

    while True:
        if curr_num == 1:
            return True

        square_sum = 0
        while curr_num > 0:
            square_sum += (curr_num % 10)**2
            curr_num = curr_num // 10

        curr_num = square_sum