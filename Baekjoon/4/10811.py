N, M = map(int, input().split(' '))

L = [i for i in range(1, N+1)]

for p in range(M):
    i, j = map(int, input().split(' '))
    LSlice = L[i-1:j]
    LSlice.reverse()
    indexCounter = 0
    for q in range(i-1, j):
        L[q] = LSlice[indexCounter]
        indexCounter += 1

for i in L:
    print(i, end=' ')