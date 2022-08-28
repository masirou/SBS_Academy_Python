# 무지개 색 순서대로 출력
Rainbow = ["red", "Orange", "Yellow", "green", "blue", "navy", "purple"]
for Index, String in enumerate(Rainbow):
    print(f"[{Index+1}] - {String}")


# 성적 평균과 최대치, 최소치 구하기
Numlist = []
while True:
    Num = int(input("(Enter negative number to stop) enter score : "))
    if Num < 0:
        break
    else:
        Numlist.append(Num)
print(
    f"Average : {round(sum(Numlist)/len(Numlist))}, maximum : {max(Numlist)}, minimum : {min(Numlist)}")
# Sum = 0
# Index = 0
# MaxValue = 0

# for i in Numlist:
#     Sum += i
#     Index += 1

# for i in Numlist:
#     if i > MaxValue:
#         MaxValue = i

# print(
#     f"Average : {Sum/Index}, maximum : {MaxValue}, minimum : {min(Numlist)}")

# 전화번호 국번만 출력

Call = input("enter Call Number : ")
Call = Call.split("-")
print(Call[1])


Number = input("(ex, 123-45-67890) enter Number : ")
Num = Number.split("-")
if len(Number) == 12:
    if Number.replace("-", ""):
        if Number[3] == "-" and Number[6] == "-":
            print("Complete")
        else:
            print("Error")
    else:
        print("Error")
else:
    print("Error")
