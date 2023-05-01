# Задание 26. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power(A, B):
    if B == 1:
        return A
    else:
        return A * power(A,B-1)
print()
a = int(input("Введите число А: "))
print()
b = int(input("Введите число B: "))
print()

print(f"{a}^{b} = {power(a,b)}")
print()