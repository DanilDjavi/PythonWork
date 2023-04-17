import random
n = int(input("Введите колbxtcndjво монет: ")) 
reshka = 0
orel = 0 
m = [random.randint(1, 2) for i in range(n)]
print(m)
for i in range(len(m)):
    if m[i] == 1:
        orel += 1
    elif m[i] == 2:
        reshka += 1
if orel < reshka:
    print("Hужно перевернуть ", orel, " монет c гравюрой орла.")
else:
    print("Hужно перевернуть ", reshka, " монет c гравюрой решки.")
