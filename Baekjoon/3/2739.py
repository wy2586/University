a = int(input())

for i in range(a):
    a = list(map(int, input().split(' ')))
    print(sum(a))