Answer = "123"

Base = input("Num : ")
Strike = 0
Out = 0
Alen = len(Answer)

for i in range(0, Alen):
    if Answer[i] == Base[i]:
        Strike = Strike+1
    else:
        for a in range(0, Alen):
            if Base[i] == Answer[a]:
                Out = Out+1

print(f"{Strike} Strike {Out} Out")