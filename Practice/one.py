import math
# from time import perf_counter

def is_prime( num : int ) -> bool :
    
    for i in range(2, math.floor(math.sqrt(num)) + 1):

        if num < 2:
            return False
        
        if num % i == 0:
            return False
        
    return True

print(is_prime(5))

# s1 = perf_counter()
# l1 = []
# for i in range(2, 50):
#     if is_prime(i):
#         l1.append(i)

# print(l1)
# s2 = perf_counter()

# time1 = s2 - s1

# s3 = perf_counter()
# l2 = [z for z in range(2, 50) if not is_prime(z)]

# print(l2)
# s4 = perf_counter()

# time2 = s4 - s3

# print(f"The time taken by normal loop: {time1:.5f}")
# print(f"The time taken by list comprehension: {time2:.5f}")

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# def my_generator():
#     for i in range(1, 11):
#         yield i

# var = my_generator()

# # print(var)
# list1 = list(var)

# print(list1)

# eleven_to_twenty = (a for a in range(11, 21))

# list2 = list(eleven_to_twenty)

# print(list2)

# prime_generators = (w for w in range(1, 20) if is_prime(w))

# list3 = list(prime_generators)
# print(list3)

# def is_even( num : int) -> bool :
#     if num %2 == 0:
#         return True
#     return False

# number = int(input("Enter a number: "))

# is_even(number)

# if is_even(number):
#     print(f"{number} is even!")
# else:
#     print(f"{number} is odd!")

# Passing a list of numbers

# def is_even( num : int) -> bool :
#         return num %2 == 0

# nums = list(map(int, input("Enter numbers separated by space: ").split()))

# for num in nums:
#     if is_even(num):
#         print(f"{num} is even!")
#     else:
#         print(f"{num} is odd!")

# Using a function

# def is_even( num : int) -> bool :
#         return num %2 == 0

# def check_numbers(numbers : list[int]) -> None :
#     for num in numbers:
#         # if is_even(num):
#         #     print(f"{num} is even!")
#         # else:
#         #     print(f"{num} is odd!")
#         print(f"{num} is even la" if is_even(num) else f"{num} is odd, yo")
        
# nums = [1, 2, 3]
# check_numbers(nums)

# Using a generator expression (even shorter)

# def is_even( num : int) -> bool :
#         return num %2 == 0

# numbers = (int(x) for x in input("Enter numbers: ").split())

# for num in numbers:
#         print(f"{num} is even!" if is_even(num) else f"{num} is odd, yo!")
