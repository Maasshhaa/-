def add_everything_up(a, b):
    try:
        resutl = a + b
        return resutl
    except TypeError:
        return str(a) + str(b) 


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))



