import sys

def book_reader(iterable_files):
    try:
        pressed_key = ''
        for file in iterable_files:
            with open(file) as current_file:
                if pressed_key == '':
                    line = current_file.readline()
                    current_chapter = ''
                    while line:
                        if line[0] == '#':
                            yield current_chapter
                            pressed_key = input()
                            while pressed_key != '':
                                pressed_key = input()
                            current_chapter = ''
                        current_chapter += line
                        line = current_file.readline()
                    yield current_chapter
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    book_reader = book_reader(['001.txt', '002.txt'])
    for chap in book_reader(['001.txt', '002.txt']):
        print(chap)

