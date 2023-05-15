S = list(map(str, input()))

for i in range(26):
    if chr(i+97) in S:
        print(S.index(chr(i+97)), end=' ')
    else:
        print(-1, end=' ')