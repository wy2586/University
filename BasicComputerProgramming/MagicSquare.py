size = int(input("마방진의 사이즈를 입력하시오(단, 홀수 정수) : "))

magic_square = [[0 for x in range(size)] for y in range(size)]

# 시작 위치 설정
firstIndex = 0
secondIndex = size // 2

# 값 할당
for num in range(1, size*size+1):
    magic_square[firstIndex][secondIndex] = num
    n_firstIndex = (firstIndex - 1) % size
    n_secondIndex = (secondIndex - 1) % size
    if magic_square[n_firstIndex][n_secondIndex]:
        firstIndex = (firstIndex + 1) % size
    else:
        firstIndex, secondIndex = n_firstIndex, n_secondIndex

# 출력
for row in magic_square:
    print(row)