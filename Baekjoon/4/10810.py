N, M = map(int, input().split(' '))
List = []
for i in range(N):
    List.append(0)

for q in range(M):
    i, j, k = map(int, input().split(' '))
    for p in range(i-1, j):
        List[p] = k

for n in List:
    print(n, end=' ')