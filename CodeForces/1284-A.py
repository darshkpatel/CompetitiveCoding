from sys import stdin, stdout, stderr
from functools import lru_cache
import math
def read():
    return stdin.readline().rstrip()

def readint():
    return int(read())

def main():
    n,m = list(map(int, read().split()))
    s = read().split()
    t = read().split()
    for x in range(readint()):
        year = readint()
        print(str(s[year%n - 1])+str(t[year%m - 1]))

main()
