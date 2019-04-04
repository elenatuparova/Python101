# wc.py
import sys

def char_count(file_content):
    chars = 0
    for line in file_content:
        chars += len(line)
    return chars

def word_count(file_content):
    words = 0
    for line in file_content:
        word_list = line.split()
        words += len(word_list)
    return words

def line_count(file_content):
    return len(file_content)

def wc(command, filename):
    file = open(filename)
    file_content = file.readlines()
    print('$ python wc.py ' + command + ' ' + filename)
    if command == 'chars':
        print(char_count(file_content))
    elif command == 'words':
        print(word_count(file_content))
    elif command == 'lines':
        print(line_count(file_content))
    file.close()


def main():
    arguments = sys.argv
    command = arguments[1]
    filename = arguments[2]
    wc(command, filename)


if __name__ == '__main__':
    main()