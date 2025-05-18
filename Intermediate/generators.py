# Generators -> function/object that allows you to generate values one at a time, only when needed, instead of calculating and storing them all at once
# Key ideas - Genrators yield values instead of "returning" them
#             Are memory efficient, doesn't store entire sequence in memory
#             Useful for larger data, infinite sequences or when you want lazy evaluation

# def generators():
#     yield 1
#     yield 2
#     yield 3

# a = generators()

# alist = list(a)
# print(alist)

# Yield pauses the function, saving its state, and resumes when next() is called again

import math

listgen = (i for i in range(0, 5))
print(listgen)
print(next(listgen))

def is_prime(num : int) -> bool :
    """Checks whether a number is prime or not"""

    sq_num = math.sqrt(num)

    for i in range(2, math.floor(sq_num) + 1):
        if num % i == 0:
            return False
    return True

# Generator expression (shorter way) - Similar to list comprehension but with ()

primegen = (i for i in range(2, 1000000000000) if is_prime(i))
print(next(primegen))
print(next(primegen))
print(next(primegen))

# print(a)

# print(next(a))
# print(next(a))
# print(next(a))

