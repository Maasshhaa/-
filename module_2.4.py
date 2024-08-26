# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []


for i in range(1, len(numbers)):

    is_prime = True
    for j in range(1, len(numbers)):
        if numbers[i] % numbers[j] == 0 and numbers[i] != numbers[j]:
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print("Список простых чисел: ", primes)
print("Список составных чисел: ", not_primes)




