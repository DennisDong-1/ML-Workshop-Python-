# Decorators -> Functions that extends the behaviour of another function without modifying the base function
# We pass the base function as an argument to the decorator
# They wrap other functions to provide additional functionality

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("You added somes sprinkles,")
    return wrapper

def add_chocolate(f):
    def w(*args, **kwargs):
        f(*args, **kwargs)
        print("and some Waffers too!")
    return w

@add_chocolate
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here, take your {flavor} ice cream!")

get_ice_cream("Strawberry")
get_ice_cream("Vanilla")