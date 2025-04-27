# people = [{
#               "name": "Dennis",
#               "roll": 5,
#               "status": "in_university",
#               "age": 23,
#               "enrolled_class": ["Python", "AAD", "Physics"]
#           },
#           {
#               "name": "Loosa",
#               "roll": 5,
#               "status": "in_university",
#               "age": 23,
#               "enrolled_class": ["Python", "AAD", "Physics"]
#           },
#           {
#               "name": "Kaushik",
#               "roll": 5,
#               "status": "passout",
#               "age": 23,
#               "enrolled_class": ["Python", "AAD", "Physics"]
#           },
#           {
#               "name": "Roshan",
#               "roll": 5,
#               "status": "in_university",
#               "age": 23,
#               "enrolled_class": ["Python", "AAD", "Physics"]
#           }]

# for i in people:
#     if (i["name"] == "Roshan"):
#         i["status"] = "expelled"

#     if (i["name"] == "Dennis"):
#         i["enrolled_class"] = ["Quantum Physics"] #Do using append

# # print(people)
# print(people[0])
# print(people[3])

#Conditionals

# while True:
#     print("Hello")
#     break

# sum = 1
# while sum <= 5:
#     print(sum)
#     sum += 1  

# l1 = [1,2,3,4,5]
# for i in l1:
#     print(i)

# count = 0
# while count <= 3:
#     print("Hello World")
#     count += 1

# for i in range(0, 4):
#     print("Hello")

#Enumerate function - gives both the index and the value from an iterable(list, tuple) while looping through it
# enumerate(iterable, start = 0)
# start -> index to start counting from(default = 0)

l1 = [11,21,31,41,51]

# for some_value in enumerate(l1):
#     # print(type(some_value))
#     # print(some_value)

#     index, element = some_value
#     print(f"Index: {index}, Element: {element}")

# for counter in enumerate(l1, start = 0):
#     print(counter)
    # print(type(i))

    # i, e = counter
    # print(f"Index: {i}, it's element: {e}")

#Functions

#First class function, variable, argument pass, return, ds ma haalna milcha
#Functions in python are first class function

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multiply(a, b):
    return a * b

def fun(op):
    if op == "add":
        return add
    if op == "sub":
        return sub
    if op == "mul":
        return multiply

operation = input("Enter your operation (add/sub/mul): ")
x = fun(operation)
print(x(5, 10))

#For next class, tuesday -> Default arguments, types of arguments, lambda functions, wrapper functions, 
#zip, map function(in-built functions)