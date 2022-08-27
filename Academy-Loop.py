"""
For문 == 반복횟수를 정확하게 알때
While문 == 반복횟수를 모르지만 반복을 종료하는 조건을 알때
"""


# 7의 배수만 출력
Num = int(input("enter the number : "))
for i in range(1, Num+1):
    if i % 7 == 0:
        print(i)

# 300원 이상이면 계속 커피를 구매하고 커피와 잔돈을 출력
Money = int(input("put the money : "))
Coffee = 0
while Money >= 300:
    Coffee = Coffee+1
    Money = Money-300
    print(f"Coffee : {Coffee} \n Money : {Money}")

# 구구단 가로로 출력
for Lnum in range(1, 10):
    for Fnum in range(2, 10):

        print(f"{Fnum} x {Lnum} = {Fnum*Lnum}", end=" \t ")
    print()

# 짝수인 단은 출려하지 말고 각 단까지만 출력
Int = int(input("enter the num : "))
sum = 0
for i in range(1, Int+1):
    sum = sum + i
print(sum)

for i in range(3, 10):
    if i % 2 == 0:
        print()
    else:
        for j in range(1, 10):
            if i >= j:
                print(f"{i} x {j} = {i*j}")
# 0부터 9 사이의 정수를 입력받고 입력된 정수가 5개가 될때까지 입력받음
Num = set([])
while True:
    a = int(input("enter between number 0 ~ 9 : "))
    if a < 10:
        Num.add(a)
        if len(Num) >= 5:
            break
    else:
        a = input("enter between number 0 ~ 9 : ")
print("complete")
sorted(Num)
print(Num)

# 1뿌터 5 사이에 존재하는 모든 정수를 역순으로 출력

for i in range(1, 6):
    print(6-i)

# 100점을 받은 학생의 점수를ㅈ ㅔ외한 나머지 학생들의 점수를 5점씩 증가시킨 score 리스트를 생성하고 출력하는 프로그램을 구현하시오 (단, 증가된 점수가 100점을 초과)
exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = exam.copy()
for i in range(0, 10):
    if score[i] != 100:
        if score[i] >= 95:
            score[i] = score[i]+(100-score[i])
        else:
            score[i] = score[i]+5
print(score)

# 3,6,9 게임 99까지 출력
for i in range(1, 100):
    if i % 10 == 0:
        if i % 3 == 0:
            print("짝", end="\n")
        else:
            print(i, end="\n")
    else:
        i = str(i)
        a = int(i[-1])
        b = int(i[0])
        if a % 3 == 0:
            if b % 3 == 0:
                print("짝짝", end="\t")
            elif a % 3 == 0:
                print("짝", end="\t")
        elif b % 3 == 0:
            print("짝", end="\t")
        else:
            print(i, end="\t")
