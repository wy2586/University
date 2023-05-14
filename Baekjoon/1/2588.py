a = int(input())
b = input()

for i in range(3):
    print(a * int(b[2 - i]))
print(a * int(b))