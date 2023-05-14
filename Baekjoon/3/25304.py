sumPrice = int(input())
a = int(input())
compPrice = 0

for i in range(a):
    a = list(map(int, input().split(' ')))
    compPrice += (a[0] * a[1])

if sumPrice == compPrice:
    print("Yes")
else:
    print("No")