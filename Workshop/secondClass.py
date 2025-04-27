# Tuples
# t1 = ("Abc", 1, 2, 3, 1, 1)

# print(t1.count(1))
# print(t1.index("Abc"))

# characters = ('a', 'b', 'x', 'y', 'z', 'i', 'o', 'e', 'u', 'p')

# for i in characters:
#     if i in ['a', 'e', 'i', 'o', 'u']:
#         print(characters.index(i))

#Dictionaires (Hash maps)

d1 = {1: "Apple",
      2: [1, 2, 3],
      3: 456}

print(d1.values())

# values = d1.values()
# l1 = list(values)
# print(l1)
# print(l1[0])

i1 = d1.items()
print(i1)

#Sets -> Unordered, no duplicates

# s1 = {1, 3, 2, 4, 5, 6, 7, 8, 9, 1, 1, 10}
# print(s1)

# s2 = {}
# print(type(s2))

# s3 = set()

# a = [1, 2]
# b = a
# b[1] = 123
# print(a)
# print(b)

# Decorators, Lambda functions(reduces code readability)
# Remaining : class(init method, getters, setters, dunder methods, inheritance), e handling(try, except, finally, 
# custom exceptions), file handling(diff modes, read, readlines, write, working with JSON CSV)

# Intermediate -> comprehensions(list, dictionary)
#             -> Generators
#             -> Zip, map
#             -> Decorators, why use them? 
#             -> SOLID
#             -> Design pattern

# Anonymous function

# square = lambda x: x * x
# print(square(4))

# cubes = lambda y: y*y*y
# print(cubes(3))

# sum = lambda num: num + 10
# print(sum(456))