N = int(input())
score = list(map(int, input().split()))
score.sort()
scoreMax = score[-1]
avg = 0

for i in range(0, len(score)):
    score[i] = (score[i]/scoreMax)*100

for l in score:
    avg += l
avg = avg/len(score)

print(avg)

