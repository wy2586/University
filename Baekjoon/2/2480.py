a = list(map(int, input().split(' ')))
a.sort(reverse=True)
a, b, c = a[0], a[1], a[2]

if a==b==c:
    print(10000 + a*1000)
elif a==b or b==c:
    print(1000 + b*100)
else:
    print(a*100)