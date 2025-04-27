# information = [
#     info1 := {"name": "Dennis",
#               "classes": ["Physics"]},
#     info2 := {"name": "Rishal",
#               "classes": ["Maths"],
#               }]

# for i in information:
#     if i["name"] == "Rishal":
#         i["classes"] = "English"

# for i in information:
#     if i["name"] == "Dennis":
#         i["classes"].append("Quantum Mechanics")
#         i["classes"].append("Python")
#         i["classes"].append("DBMS")

# print(info1["classes"])

#Functions in python are all first class functions(first class citizens), are treated like any other object
# first class functions can be ->
#       assigned to variables
#       passed as arguments to other functions
#       returned from other functions
#       stored in data structures(lists, dicts)

# def fun_bye():
#     print("Goodbye lads!")

# def fun_greet(name, f1):
#     print(f"{name} signing off,")
#     f1()

# n = input("Enter the name: ")
# fun_greet(n, fun_bye) #passing as argument


# def fun_add(n1, n2):
#     return n1 + n2
# def fun_mul(n1, n2):
#     return n1 * n2

# def fun_operation(operator):
#     if operator == "+":
#         return fun_add #returning from other functions
#     if operator == "*":
#         return fun_mul

# num1= int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# op = input("Enter the operator(+/*): ")

# ref_fun = fun_operation(op) #assigning to variables

# print(ref_fun(num1, num2))

# data_str =  [ref_fun, "Machine", fun_operation] #storing in data structures
# print(data_str)

# NEXT --->>>

#Types of arguments ->
        # positional -> args are assigned based on their position
        # keyword -> order doesn't matter
        # default -> uses default if not given, else overrides
        # variable length (args, kwargs)
            # args is a tuple of all extra arguments
            # kwargs is a dictionary of all extra keyword arguments
        # keyword-only

# def info(name, age = 23):
#     print(f"Hello {name}, you're {age} years old.")

# # n = input("Enter your name: ")
# # a = int(input("Enter your age: "))

# info("Dennis")
# info(age = 20, name = "Dennis") #keyword args, order doesn't matter

# Args and Kwargs

# def nums(*numbers):
#     for i in numbers:
#         print(i)

# nums(1, 2, 3, "Dennis")

# def add(*numbers):
#     total = sum(numbers)
#     print(total, "is the total sum.")

# add(5, 5, 5)

# def add(*numbers):

#     total = 0
#     for i in numbers:
#         total += i
#     return total

# print(add(1, 2, 3, 4, 5))

# def print_info(**infos):
#     for k, v in infos.items():
#         print(f"{k}: {v}")

# # print_info(one = "Apple", two = "Banana", three = "Cherry")
# print_info(name = "Dennis", age = "23", address = "Samakhusi")

# Keyword-only arguments

# Lambda functions - anonymous/nameless functions, are short, simple and super useful for quick operations

# import math
# sq_rt = lambda x: math.sqrt(x)
# sum = lambda a, b, c: a + b + c

# print(sq_rt(16))
# print(sum(5, 10, 15))

# Wrapper function -> wraps another function, add extra behaviour, before or after calling the original function

def wrapper(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner

def print_msg():
    print("Hey man!")

w = wrapper(print_msg)
w()