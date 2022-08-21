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
