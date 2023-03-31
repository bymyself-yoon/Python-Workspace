student = int(input("학생 수 입력: "))

all_score = []
sum = 0
avg = 0
max = 0

for i in range(0, student, 1):
    score = float(input('점수 입력: '))
    all_score.append(score)

for i in all_score:
    sum += i

avg = sum / student
all_score.sort()



print("점수 평균은 {}점입니다.".format(avg))
for i in range(0, student, 1):
    print(i+1, "등: ", all_score[i])

