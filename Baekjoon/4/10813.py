N, M = map(int, input().split(' '))

List = [i for i in range(1, N+1)]

for e in range(M):
    i, j = map(int, input().split(' '))
    List[i-1], List[j-1] = List[j-1], List[i-1]

for i in List:
    print(i, end=' ')