calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string1):
    count_calls()
    return (len(string1),string1.upper(), string1.lower())

def is_contains(string2, my_list):
    count_calls()
    list_low = [x.lower() for x in my_list]
    if string2.lower() in list_low:
        return True
    else:
        return False

print(string_info("Владимир"))
print(string_info("HelloHello"))
print(is_contains("Урбан",["УРбан", "бан", "урбеч"]))
print(is_contains("Урбан",["барабан", "бан", "урбеч"]))
print(calls)