# Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список)
# размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))
value = input("Введите значение матрицы: ")

result = get_matrix(n, m, value)
print(result)