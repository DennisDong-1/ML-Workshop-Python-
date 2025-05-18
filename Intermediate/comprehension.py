# Design pattern -> Factory, Singleton DP

import math
from time import perf_counter

def is_prime(num : int) -> bool :
    """Checks whether a number is prime or not"""

    sq_num = math.sqrt(num)

    for i in range(2, math.floor(sq_num) + 1):
        if num % i == 0:
            return False
    return True

# list1 = []
# for i in range(2, 100):
#     if is_prime(i):
#         list1.append(i)

# is_prime(i) #No idea what this line is doing!
# print(list1)

start_time = perf_counter()
list2 = [i for i in range(2, 1000000) if is_prime(i)]
end_time = perf_counter()

total_duration = end_time - start_time

# print(list2)
print(start_time)
print(end_time)
print(f"The function took: {total_duration} seconds!")