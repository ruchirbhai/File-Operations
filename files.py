import sys


f = open(sys.argv[1], mode='rt', encoding='utf-8')

for line in f:
    #print(line)
    #print intorduces its own newline while printing thus the output comes out to be double spaced
    sys.stdout.write(line)

f.close()