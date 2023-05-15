a, b = input().split(' ')
a, b = list(a), list(b)
aInt = ''
bInt = ''

a.reverse()
b.reverse()
for i in range(0, len(a)):
    aInt += a[i]
for i in range(0, len(b)):
    bInt += b[i]

aInt, bInt = int(aInt), int(bInt)

if aInt > bInt:
    print(aInt)
else:
    print(bInt)