# cat2.py
import sys

def cat2(arguments):
    command = '$ python cat.py '
    for argument in arguments:
        command = command + str(argument) + ' '
    print(command)
    for argument in arguments:
        file = open(argument)
        file_content = file.readlines()
        for line in file_content:
            print(line.strip('\n'))
        print('\n')
        file.close()


def main():
    arguments = sys.argv
    cat2(arguments[1:])

if __name__ == '__main__':
    main()