
def absolute_sum(data_structure, list_sum = []):
    for i in data_structure:
        type_now = type(i)
        if type_now == list or type_now == tuple:
            list_sum += list(i)
        if type_now == dict:
            list_sum += list(i.keys())
            list_sum += list(i.values())
        if type_now == str:
            list_sum.append(len(i))
        if type_now == set:
            i = list(*i)
            list_sum += i
        if type_now == int:
            list_sum.append(i)
    if all(isinstance(i, int) for i in list_sum):
        print(sum(list_sum))
    else:
        absolute_sum(list_sum, [])

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
print(f'данная структура: {data_structure}')
print('Cумма всех чисел и длин всех строк:'),
absolute_sum(data_structure)


data_structure2 = [[1, 1, {'ddd': 1}], 'sdwaoo', [{(1, 1, (3))}]]
print(f'данная структура: {data_structure2}')
print('Cумма всех чисел и длин всех строк:'),
absolute_sum(data_structure2, list_sum=[])

