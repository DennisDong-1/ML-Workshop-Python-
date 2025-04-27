# class methods -> allow operations related to the class itself
#               -> take (cls) as the first parameter, which represents the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #Instance method
    def get_info(self):
        return f"{self.name}'s GPA is {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total no. of students = {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa is: {cls.total_gpa/cls.count:.2f}"

s1 = Student("Dennis", 3.60)
s2 = Student("Sam", 4)
s3 = Student("Ram", 3.80)
s4 = Student("Hari", 3.90)

print(Student.get_count())
print(Student.get_average_gpa())

# Instance - Best for operations on instances of the class (objects)
# Static - Best for utility functions that donot need access to class data
# Class - Best for class-level data or require access to the class itself