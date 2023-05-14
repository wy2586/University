while True:
    try:
        a = list(map(int, input().split()))
        print(a[0] + a[1])
    except:
        break