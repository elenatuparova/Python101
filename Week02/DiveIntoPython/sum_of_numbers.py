import re
def sum_of_numbers(input_string):
    numbers_list = re.findall(r'\d+', input_string)
    return sum(int(num) for num in numbers_list)