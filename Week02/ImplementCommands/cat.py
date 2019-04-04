# cat.py
import sys

def cat(arguments):
    file = open(arguments)
    file_content = file.readlines()
    print('$ python cat.py '+ arguments)
    for line in file_content:
        print(line.strip('\n'))
    file.close()

def main():
    arguments = sys.argv
    cat(arguments[1])

if __name__ == '__main__':
    main()