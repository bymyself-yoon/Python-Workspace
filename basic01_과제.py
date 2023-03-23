print("*********** 계산기 ***********")

num1, num2 = input("실수 또는 정수 2개 입력: ").split()
num1 = eval(num1)
num2 = eval(num2)

sum = num1 + num2
print('두 수의 합: ', sum)
if(num1 >= num2):
    minus = num1 - num2
else: minus = num2 - num1
print('두 수의 차: ', minus)
multi = num1 * num2
print("두 수의 곱: ", multi)
divide = num1 / num2
print("두 수의 몫: ", divide)

print('******************************')