def print_params(a = 4, b = "строка", c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list=[78, "ДОброе утро", False]
print_params(*values_list)

values_dict = {"a":14, "b":"domoy", "c":False}
print_params(**values_dict)

values_list_2=[68, "Russia"]
print_params(*values_list_2, False)