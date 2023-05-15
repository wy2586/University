T = int(input())

for i in range(T):
    R, S = input().split(' ')
    R = int(R)
    for i in S:
        print(i*R, end='')
    print()