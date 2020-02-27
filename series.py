"""read and print integer series"""
import sys


def read_series(filename):
    try:
        #refactor Code to use comprehension
        f = open(filename, mode='rt', encoding='utf-8')
        return [int(line.strip()) for line in f]

    finally:
        f.close()

def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(filename=sys.argv[1])
