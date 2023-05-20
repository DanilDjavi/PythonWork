# Задание 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

def count_vowels(word):
    vowels = "aeiouyAEIOUY"
    return len([char for char in word if char in vowels])

print()
poem = input("Введите стихотворение: ")
print()
phrases = poem.split()
num_vowels = [count_vowels(phrase.replace('-', '')) for phrase in phrases]

# проверяем, все ли числа равны
if all(num == num_vowels[0] for num in num_vowels):
    print("Парам пам-пам")
else:
    print("Пам парам")
print()