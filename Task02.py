# Задание №2 Найдите сумму цифр трехзначного числа

print()
number = int(input("Введите трехзначное число: "))
print()
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print("Сумма цифр числа:", sum)
print()
