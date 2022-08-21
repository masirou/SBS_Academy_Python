
f = open("file.txt", encoding="UTF-8")
Mylist = list(f.read().split())
count = {}

for i in Mylist:
    try:
        count[i] += 1
    except:
        count[i] = 1
print(count)
