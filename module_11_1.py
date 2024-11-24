import sys


def introspection_info(obj):
    print(f'Тип объекта: {type(obj)}')
    print(f'Атрибуты, методы, функции и переменные объекта: {dir(obj)}')
    try:
        module = obj.__module__
        print(f'Модуль, которые принадлежит объекту: {module}')
    except:
        print("данный объект не имеет модуля\n")


introspection_info(sys)

class SampleClass:
    def method1(self):
        pass

    def method2 (self):
        pass


sample_obj = SampleClass()
result = introspection_info(sample_obj)

