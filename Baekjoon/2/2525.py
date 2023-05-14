a = list(map(int, input().split(' ')))
H, M = a[0], a[1]

needTime = int(input())

M += H*60
M += needTime
H = M//60
M = M%60 

if H >= 24:
    H = H%24

print(H, M)