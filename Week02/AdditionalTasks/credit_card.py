def is_credit_card_valid(number):
    str_number = str(number)

    if len(str_number) % 2 == 0:
        return False

    digits = [digit for digit in str_number]
    index = 1
    while index <= len(digits) - 2:
        digit_to_double = int(digits[index]) * 2
        digits[index] = str(digit_to_double)
        index += 2
    new_str_number = ''.join(digits)
    new_digits = [int(digit) for digit in new_str_number]
    
    if sum(new_digits) % 10 == 0:
        return True
    return False