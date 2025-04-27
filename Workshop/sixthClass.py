#Dictionary/List comprehension
l1 = [1, 2, 3, 4, 5]

# cubes = [x**3 for x in range(5)]
# print(cubes)

# l3 = [i + 10 for i in l1 if i%2 == 0] #Filtering even
# print(l3)

# fruits = ["Apple", "Banana"]
# uppercased = [item.upper() for item in fruits] #Applying function to items
# print(uppercased)

# matrix = [[x * y for y in range(1,4)] for x in range(1,11)] #Nested list comprehension
# print(matrix)

# def mul_table(n = 5):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")

# mul_table()

# l4 = [[1,2,3], [4,5,6]]

# flat = [item for sublist in l4 for item in sublist] #Flattening a nested list
# # flat = [i for j in l4 for i in j]
# print(flat) 

# original = {"1": "Mercedes", "2": "BMW", "3": "Tesla"}

# swapped = {value: key for key, value in original.items()}
# s2 = {i: j for j, i in original.items()}
# print(s2)
# print(swapped)

# d1 = { i: i*2 for i in l1 if i%2 != 0}
# print(d1)

# d2 = { i: i*3 for i in l1}
# print(d2)

# arr_dict = {
#     1: [1,2,3],
#     2: [4,5,6],
#     1: [7,8,9]
# }

# print(arr_dict[1])
# print(arr_dict)

# d2 = {
#     (1,2,3): "Attack", #tuple cause is hashable
#     (4,5,6): "Next Level"
# }

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"The name is: {self.name}, age is {self.age}")

# class Student(Person):
#     def __init__(self, name, age, roll, grade):
#         self.roll = roll
#         self.grade = grade
#         super.__init__(name, age)

#     def get_info(self):
#         print(f"The name of the student is: {self.name}, age is {self.age}, roll is {self.roll}, with grade {self.grade}")

# s1 = Student("Ram", 23, 5, "A")

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return self.x + other.x, self.y + other.y
#     # def show(self):
#     #     return self.x + self.y

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# print(p1 + p2)
# print(p1.show())
# print(p2.show())