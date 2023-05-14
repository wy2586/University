maxNum = 0
repeatNum = 0
temp = 0

for i in range(9):
    temp += 1
    a = int(input())
    if a > maxNum:
        maxNum = a
        repeatNum = temp

print(maxNum)
print(repeatNum)

