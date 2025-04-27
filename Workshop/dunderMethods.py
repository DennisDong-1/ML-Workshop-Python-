# Dunder methods -> double underscore methods, magic methods since they let you customize how objects behave
# used to define behaviour for -> object creation, operator overloading, string representation, iteration...
# common -> init, str, repr, len, getitem, setitem, iter, next, eq, lt, add, sub

# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f"Your name is {self.name}"
    
#     def __len__(self):
#         return len(self.name)
    
# person1 = Person("Alexander")

# print(person1)
# print(len(person1))

#Operator overloading example

class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __str__(self):
        return str(self.value)
    
    def __eq__(self, other):
        if isinstance(other, Number): #check type, checks if other is a number
            return self.value == other.value #compare values
        return False
    
a = Number(5)
b = Number(5)
print(a+b)
print(a == b)

# class Sum:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# n1 = Sum(10)
# n2 = Sum(15)
# print(n1 + n2)

# getitem -> indexing(obj[key])
# setitem -> setting with index(obj[key] = value)
# lets you treat your objects lists/dictionaries with []

# Accessing like a list/dict

# class Container:
#     def __init__(self):
#         self.data = {1: "Apple", 2: "Banana", 3: "Cherry"}
#     def __getitem__(self, key):
#         return self.data[key]

# c = Container()
# print(c[1]) #when you do c[1], python internally calls c.__getitem__(1)

# Setting values with []

# class Sports:
#     def __init__(self):
#         self.data = {}
#     def __setitem__(self, key, value):
#         self.data[key] = value
#     def __getitem__(self, key):
#         return self.data[key]

# s = Sports()
# s[1] = "Football"
# s[2] = "Basketball"
# s[3] = "Volleyball"

# print(s[3])

# Combining them for a list like class

class CustomList:
    def __init__(self, items):
        self.items = items
    def __getitem__(self, index):
        return self.items[index]
    def __setitem__(self, index, value):
        self.items[index] = value

cl = CustomList(["Abc", "Xyz", 123])
print(cl[1])
cl[1] = 456
print(cl[1])