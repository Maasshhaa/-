import sys


def introspection_info(obj):
    print(f'Тип объекта: {type(obj)}')

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__") and not method.startswith("_")]
    print(f'Методы объекта: {methods}')

    attributes = [method for method in dir(obj) if callable(getattr(obj, method)) and method.startswith("__") or method.startswith("_")]
    print(f'Атрибуты объекта: {attributes}')

    try:
        module = obj.__module__
        print(f'Модуль, которые принадлежит объекту: {module}\n')
    except:
        print("данный объект не имеет модуля\n")


class SampleClass:
    def method1(self):
        pass

    def method2 (self):
        pass


sample_obj = SampleClass()
introspection_info(sample_obj)

introspection_info(sys)
