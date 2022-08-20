# 입력한 값과 Answer에 있는 자리와 수가 같을땐 strike를 증가,
# 입력한 값이 Answer안에 있는데 자리가 다른땐 Out을 증가
# 아무것도 같지 않으면 아무것도 증가시키지 않음.

Answer = "123"

Base = input("Num : ")
Strike = 0
Out = 0

for i in range(0, len(Answer)):
    if Answer[i] == Base[i]:
        Strike = Strike+1
    elif Base[i] in Answer:
        Out = Out+1

print(f"{Strike} Strike {Out} Out")
