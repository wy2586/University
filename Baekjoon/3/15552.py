import sys

n = int(input())

for i in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(a[0] + a[1])
