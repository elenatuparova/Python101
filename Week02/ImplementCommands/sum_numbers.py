# sum_numbers.py
import sys

def sum_numbers(filename):
    file = open(filename)
    file_content = file.readlines()[0]
    numbers = [int(number) for number in file_content.split()]
    print('$ python sum_numbers.py ' + filename)
    print(sum(numbers))
    file.close()

def main():
    arguments = sys.argv
    filename = arguments[1]
    sum_numbers(filename)

if __name__ == '__main__':
    main()