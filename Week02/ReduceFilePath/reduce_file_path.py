import sys

def reduce_file_path(path):
    reduced_path = ''
    dirs = path.split('/')
    dirs_reduced = []
    for dir in dirs:
        if dir == '..' and len(dirs_reduced) != 0:
            dirs_reduced.pop()
        if dir != '.' and dir != '..' and dir != '':
            dirs_reduced.append(dir)
    for dir in dirs_reduced:
        reduced_path += '/'
        reduced_path += dir
    if len(dirs_reduced) == 0:
        reduced_path = '/'
    return reduced_path


def main():
    arguments = sys.argv
    print(reduce_file_path(arguments[1]))

if __name__ == '__main__':
    main()