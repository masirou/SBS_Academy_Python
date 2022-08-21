import operator

# 차량번호 뒤에 숫자 4자리만 출력
Num = "243가9124"
print(Num[-4:])

# 10~99자리의 수에서 십의자리, 일의자리를 찾기
NumI = input("enter a 10 ~ 99 num : ")
print(f"Ten : {NumI[0]}")
print(f"One : {NumI[1]}")

# 초 분,시간으로 바꾸기
Second = int(input("enter the seconds : "))
Minute = 0
Hour = 0
while Second >= 3600:
    Hour = Hour + 1
    Second = Second - 3600
while Second >= 60:
    Minute = Minute + 1
    Second = Second - 60
print(f"Hour : {Hour}\nMinute : {Minute}\nSeconds : {Second}")

# file.txt 파일에서 텍스트를 불러와서 단어 빈도수 랭킹, 중복되는 값 찾기
f = open("file.txt", encoding="UTF-8")
list = f.read().split()

Tdict = {}
for i in list:
    Tdict[i] = list.count(i)
sdict = sorted(Tdict.items(), key=operator.itemgetter(1), reverse=True)
c = len(sdict)
for i in range(0, c):
    print(f"{i+1}. {sdict[i][0]} \t{sdict[i][1]}")

overlap = []
for i in list:
    if list.count(i) > 1:
        overlap.append(i)
        for a in range(list.count(i)-1):
            list.remove(i)
print(overlap)
