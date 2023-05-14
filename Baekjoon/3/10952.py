import sys

while True:
    a = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    if a[0] == 0 and a[1] == 0:
        break
    else:
        print(a[0] + a[1])