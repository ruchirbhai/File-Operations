"""read and print integer series"""
import sys


def read_series(filename):
    try:
        #series = []
        f = open(filename, mode='rt', encoding='utf-8')
        #for line in f:
        #    a = int(line.strip())
        #    series.append(a)
        #refactor Code to use comprehension
        return [int(line.strip()) for line in f]

    finally:
        f.close()

def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == '__main__':
    main(filename=sys.argv[1])
