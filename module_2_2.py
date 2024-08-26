first = input("Введите первое число - ")
second = input("Введите второе число - ")
third = input("Введите третье число - ")

print("\n""Число совпадений:")
if first != second and second != third and first != third:
    print(0)
elif first == second == third:
    print(3)
else:
    print(2)
