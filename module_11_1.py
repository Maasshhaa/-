import numpy as np
import requests

#примеры работы библиотеки numpy
a = np.array([1, 2, 3], dtype='int32')
print(a)
print(a.ndim)

с = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(с.shape)

a = np.zeros(10)
print(a)

c = np.full((4, 4), 1)
print(c)

#примеры работы библиотеки requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)


response = requests.get(
    'https://urban-university.ru/members/courses/course999421818026/20231222-0000domasnee-zadanie-po-teme-obzor'
    '-storonnih-bibliotek-python-400269495184')
if response.status_code == 200:
    print("GET-запрос успешен!")
else:
    print("Ошибка:", response.status_code)

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
if response.status_code == 201:
    print("POST-запрос успешен!")
    print(response.json())
else:
    print("Ошибка:", response.status_code)