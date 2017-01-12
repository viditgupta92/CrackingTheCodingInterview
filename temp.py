import math
a = 0b1110
b = 0b101
res = len((a > b) * b + (b > a) * a)
diff = abs(len(a) - len(b))
lst = []
for i in range(res):
    if (a[i] == 1 and b[i] == 0) or (a[i] == 0 and b[i] == 1):
        lst[i] = 1
    else:
        lst[i] = 0
for j in range(i, i + diff + 1, 1):
    lst[i] == 0

print("".join(lst))