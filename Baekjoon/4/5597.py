stuNum = [i for i in range(1, 31)]

for i in range(28):
    Num = int(input())
    stuNum.remove(Num)

stuNum.sort()
print(stuNum[0])
print(stuNum[1])