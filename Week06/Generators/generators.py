import sys

#chain
def chain(iterable_one, iterable_two):
    for item in iterable_one:
        yield item
    for item in iterable_two:
        yield item


#compress
def compress(iterable, mask):
    for pair in zip(iterable, mask):
        if pair[1] == True:
            yield pair[0]


#cycle
def cycle(iterable):
    while True:
        for item in iterable:
            yield item


if __name__ == '__main__':
    lst1 = list(chain([2, 5, 6], [3, 5, 8]))
    print(lst1)

    lst2 = list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
    print(lst2)

    endless = cycle(range(1, 10))
    for item in endless:
        print(item)

