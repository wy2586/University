n = int(input())
a = list(map(int, input().split(' ')))
v = int(input())
result = 0

for i in a:
    if i == v:
        result += 1

print(result)