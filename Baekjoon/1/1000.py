# 두 정수 A와 B를 입력받은 다음, A+B

# 1차 | 31256kb, 44ms
# a = input().split(" ")
# print(int(a[0]) + int(a[1]))

# 2차 | 31256kb, 44ms
a = map(int, input().split(' '))
print(sum(a))