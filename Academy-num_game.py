import random

Rnum = random.randint(1,100)

while True:
    Inum =int(input("Number : "))
    if Inum < Rnum:
        print("Enter Num is Small")
    if Inum > Rnum:
        print("Enter Num is big")
    if Inum == Rnum:
        print("It's Answer!!")
        break