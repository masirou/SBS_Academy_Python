# 1, 100까지의 랜덤한 수를 Up,Down하면서 맞추는 게임

import random

Rnum = random.randint(1, 101)

while True:
    Inum = int(input("Number : "))
    if Inum < Rnum:
        print("UP")
    if Inum > Rnum:
        print("Down")
    if Inum == Rnum:
        print("It's Answer!!")
        break
