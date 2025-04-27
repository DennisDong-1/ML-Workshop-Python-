# Duck typing -> objects must have minimum necessary attributes/methods
#                "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:

    alive = False

    def speak(self):
        print("Honk!")

animals = [Dog(), Cat(), Car()]
for a in animals:
    a.speak()
    print(a.alive)