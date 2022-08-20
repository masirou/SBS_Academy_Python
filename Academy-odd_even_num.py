odd = 0
even = 0
for i in range(1, 101):
    if i % 2 == 0:
        odd = odd + i
    else:
        even = even + i
print(f"Odd num : {odd}")
print(f"Even num : {even}")
