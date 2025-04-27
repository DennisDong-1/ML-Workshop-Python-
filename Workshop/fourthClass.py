def calc(*num1, func):
    a, b = num1
    result = func(a, b)
    return result

def add_element(a, b):
    return a + b
def mul_element(a, b):
    return a * b
def sub_element(a, b):
    return a - b
def divide_element(a, b):
    return a / b

print(calc(4, 5, func = add_element))