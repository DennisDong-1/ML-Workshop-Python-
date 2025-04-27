# class variables -> defined outside the constructor, shared among all instances of a class
# allows you to share data among all objects created from that class

class Student:
    
    class_year = 2021
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

s1 = Student("Dennis", 23)
s2 = Student("Likhil", 22)
s3 = Student("Pratik", 22)

print(f"Our class of {Student.class_year} has {Student.num_students} students.")
print(s1.name)
print(s2.name)
print(s3.name)