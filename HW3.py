# угадывание чисел

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10
a = 1
b = 0

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Угадайте число от 0 до 1000. У вас 10 попыток.")

for atempt in range(MAX_ATTEMPTS):
    b = int(input(f"Попытка №{atempt + a}: "))

    if b < num:
        print("Загаданное число больше.")
    elif b > num:
        print("Загаданное число меньше.")
    else:
        print("Поздравляю! Вы угадали число!")
        break

if b != num:
    print("Попытки закончились, мне жаль =( Загаданное число было:", num)
