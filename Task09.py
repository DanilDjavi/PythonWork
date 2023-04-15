x = int(input("Введите число: ")) # 0 1 1 2 3 5 8 13 21
n1 = 0                            # 1 2 3 4 5 6 7  8  9
n2 = 1
s = 0
k = 0
i = 3
while i <= x:
    s = n1 + n2
    k = n2
    n2 = s
    n1 = k
    i += 1
print(s)