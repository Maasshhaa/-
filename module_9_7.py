def is_prime(func):
    def wrapper(one, two, three):
        res = func(one, two, three)
        prime = 'Простое'
        for i in (range(2, res)):
            if res % i == 0:
                prime = 'Составное'
        return f'{prime} \n{res}'
    return wrapper


@is_prime
def sum_three(one, two, three):
    res = one + two + three
    return res


result = sum_three(2, 3, 6)
print(result)