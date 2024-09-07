# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число
# number и подсчитывает произведение цифр этого числа.

def get_multiplied_digits(n):
    str_number = str(n)
    first = int(str_number[0])
    if len(str_number) == 1:
        return n
    elif len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(9365))
print(get_multiplied_digits(40203))

