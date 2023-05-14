a = list(map(int, input().split(' ')))
a, b, c = a[0], a[1], a[2]

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)