from sys import argv


def sum(first, second):
    print(int(first) + int(second))


sum(first=argv[1], second=argv[2])


