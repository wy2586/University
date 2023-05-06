def isLeapYear(year):
    '''
    윤년 여부를 계산
    '''
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
def findLastDay(year, month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year) == True:
        m[1] = 29
    else:
        m[1] = 28
    
    return m[month-1]

def sumTotalDay(year, month):
    '''
    예 : 인수로 2023, 4를 입력
    -> 2023년 4월까지의 날짜 계산
    -> 2022년의 총 일수 + 2023년 4월까지 일수
    '''
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totalDay = 0
    for i in range(1, year):        # year-1년까지의 총 일수
        if isLeapYear(i) == True:
            m[1] = 29
        else:
            m[1] = 28
        for j in range(0, 12):
            totalDay += m[j]
    
    if isLeapYear(year) == True:
        m[1] = 29
    else:
        m[1] = 28

    for i in range(0, month):  # year년의 month 달까지의 총 일수
        totalDay += m[i]
    
    return totalDay

def selectDay(totalDay):
    '''
    총 일수를 인수로 받아 끝난 요일을 구함
    0 : 일, 1 : 월, 2 : 화, 3 : 수, 4 : 목, 5 : 금, 6 : 토
    만약 2023년 4월까지의 totalDay를 전달하여 0을 받았다면
    2023년 4월은 일요일에 끝나고 2023년 5월은 월요일부터 시작함.
    '''
    result = totalDay % 7
    return result

def makeCalendar(year, month):
    startDay = selectDay(sumTotalDay(year, month-1)) + 1
    lastDay = findLastDay(year, month)

    print(f"         {year}년 {month}월")
    print(f"===================================")
    print(f"Sun   Mon   Tue   Wed   Thr   Fri   Sat")
    print('      '*startDay, end=' ')
    for i in range(1, lastDay + 1):
        print(f"{i: >2}", "  ", end=' ')
        startDay += 1
        if startDay == 7:
            startDay = 0
            print('\n')

makeCalendar(2023, 3)