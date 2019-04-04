# generate_numbers.py
import sys
from random import randint


def generate_numbers(filename, numbers):
    print('$ python generate_numbers.py ' + filename + ' ' + numbers)
    file = open(filename, 'w+')
    random_numbers = ''
    for i in range(int(numbers)):
        random_numbers += str(randint(1, 1000)) + ' '
    file.write(random_numbers)
    file.close()

def main():
    arguments = sys.argv
    filename = arguments[1]
    numbers = arguments[2]
    generate_numbers(filename, numbers)

if __name__ == '__main__':
    main()