# Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный
# пароль result, для одного введённого числа.

import random
first_stone = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(first_stone)
print(f'Значение первого поля: {n}')

result = []
multiple = []
for i in range(18):
    if n % first_stone[i] == 0:
        multiple.append(first_stone[i])
        for second_digit in range(18, 1, -1):
            for first_digit in range(1, 18):
                if second_digit == first_digit:
                    break
                elif first_digit + second_digit == multiple[-1]:
                    result.extend([first_digit, second_digit])


print(f'Все подходящие делители числа {n}: {multiple}')
print("Нужный пароль: ", *result)

