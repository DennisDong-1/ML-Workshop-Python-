# Static methods -> method that belongs to a class rather than any object from that class (instance)
                  # usually used for general utility functions that donot need access to class data
# Instance methods -> Best for operations on instances of the class (objects)

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Cook", "Manager", "Cashier", "Accountant"]
        return position in valid_positions

e1 = Employee("Dennis", "Manager")
e2 = Employee("Likhil", "Cook")
e3 = Employee("Pratik", "Cashier")
print(e1.get_info())
print(e2.get_info())
print(e3.get_info())
print(Employee.is_valid_position("Manager"))