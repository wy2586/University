import sys

n = int(input())

for i in range(1, n+1):
    a = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(f"Case #{i}: {a[0] + a[1]}")