def reverse_string(string):
    reversed_str = ''
    len_str = len(string)

    for index in range(len_str):
        reversed_str += string[len_str - 1 - index]

    return reversed_str

def check_is_palindrome(number):
    str_number = str(number)
    return str_number == reverse_string(str_number)

def get_largest_palindrome(n):
    current_number = n - 1
    while current_number >= 0:
        if check_is_palindrome(current_number):
            return current_number
        current_number -= 1