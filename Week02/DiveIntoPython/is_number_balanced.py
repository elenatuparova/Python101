def sum_digits_of_string_number(string_number):
    return sum([int(digit) for digit in string_number])

def is_number_balanced(number):
    str_number = str(number)
    len_of_number = len(str_number)

    if (len_of_number) == 1:
        return True

    skip_middle_index = 1 if len_of_number % 2 == 1 else 0
    left_part = str_number[:len_of_number // 2]
    right_part = str_number[len_of_number // 2 + skip_middle_index:]

    return sum_digits_of_string_number(left_part) == sum_digits_of_string_number(right_part)