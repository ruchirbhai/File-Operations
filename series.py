"""read and print integer series"""
import sys


def read_series(filename):
    # refactor Code to use comprehension
    # edit 2: Use with block and remove explict close

    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]

def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(filename=sys.argv[1])
