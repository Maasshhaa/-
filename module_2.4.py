# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


for i in numbers:

    is_prime = True
    for j in numbers:
        if i % j == 0 and i != j and i != 1 and j != 1:
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)

print("Список простых чисел: ", primes)
print("Список составных чисел: ", not_primes)




