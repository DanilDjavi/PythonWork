# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

lst = [2, 6, 13, 7, 9, 10, 18]
print()
min_val = int(input("Введите минимум: "))
print()
max_val = int(input("Введите максимум: "))
print()
result = [i for i, val in enumerate(lst) if min_val <= val <= max_val]

print("Индексы элементов списка, удовлетворяющих заданному диапазону: ", result) # должно вывести [1, 2, 3, 4]
print()