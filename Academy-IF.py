# 점수를 입력받아 학점을 출력  A = 100 ~ 90 || B = 89 ~ 80 || C = 79 ~ 70 || D = 69 ~ 60 || F = 59 ~ 0
Score = int(input("enter the Score : "))

if Score >= 90:
    Credit = "A"
elif Score >= 80:
    Credit = "B"
elif Score >= 70:
    Credit = "C"
elif Score >= 60:
    Credit = "D"
elif Score >= 0:
    Credit = "F"
print(f"Score is {Score}, Credit is {Credit}")

# 임의의 정수를 입력받은 뒤 해당 값이 3의 배수인지 아닌지를 판별
Sum = input("enter the Sum : ")


if int(Sum) % 3 == 0:
    print(f"{Sum} is a multiple of 3")
else:
    print(f"{Sum} is not a multiple of 3")

# 임의의 정수 3개를 입력받아 그 중에서 가장 큰 수를 출력
Num1 = input(f"[1] enter the Num : ")
Num2 = input(f"[2] enter the Num : ")
Num3 = input(f"[3] enter the Num : ")
if Num1 > Num2:
    if Num1 > Num3:
        print(Num1)
if Num2 > Num3:
    if Num2 > Num1:
        print(Num2)
if Num3 > Num1:
    if Num3 > Num2:
        print(Num3)

# 차량번호가 짝수로 끝나면 운행가능, 홀수로 끝나면 운행불가, 차량번호는 237가1234와 같은 형식
CarNum = input("(ex, 237가1234) enter the Car Number : ")
if int(CarNum[5:]) % 2 == 0:
    print(f"car's number {CarNum} is available today")
else:
    print(f"car's number {CarNum} is Unavailable today")
