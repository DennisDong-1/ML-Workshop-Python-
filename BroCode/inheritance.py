# Multiple inheritance -> a child inherits from multiple parents C(A, B)

# Multilevel inheritance -> inherits from a parent class which inherits from another parent C(B) <- B(A) <- A

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

r = Rabbit("Bunny")
h = Hawk("Tony")
f = Fish("Nemo")

f.hunt()