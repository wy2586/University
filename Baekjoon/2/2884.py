a = list(map(int, input().split(' ')))
H, M = a[0], a[1]

M += H*60
M -= 45
H = M//60
M = M%60

if H < 0:
    H = 23

print(H, M)