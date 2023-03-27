Eng = float(input('영어 점수 입력: '))
Math = float(input('수학 점수 입력: '))
Kor = float(input('국어 점수 입력: '))

score = [Eng, Math, Kor]

for i in score:
    if(i > 60):
        print(i,'점은 합격입니다!')
    else:
        print(i, '점은 불합격입니다.')
