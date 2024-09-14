
def  test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function() #функция работает
inner_function() #функция вне области видимости
