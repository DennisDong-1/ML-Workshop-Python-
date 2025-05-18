# Prime check

import math

# def is_prime(num):
# def is_prime( num : int) -> bool:
#     for i in range(2, math.floor(math.sqrt(num) + 1)):
#         if num % i == 0:
#             return False
#     return True

# l1 = []
# for i in range(2, 15):
#     if is_prime(i):
#         l1.append(i)

# print(l1)

# l2 = [i for i in range(1, 11)]
# print(l2)

# d1 = {i: i**2 for i in range(1, 6)}
# print(d1)

# d1 = {i: i**2 for i in range(1, 11) if i%2 == 0}
# print(d1)

# prices = {'apple': 100, 'banana': 200}

# create new d with 10% price increase

# new_d = {key: value * 1.1 for key, value in prices.items()}

# new_d = {i: j * 1.2 for i, j in prices.items()}

# print(new_d) 

# c = 0

# while c < 11:
#     print(c)
#     c += 1

# l1 = [1,2,3,4,5,6,7,8,9,10]
# print(l1[3:6:1])

# def f(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * f(n-1)
    
# print(f(5))

# def f2(n):
#     r = 1
#     for i in range(1, n+1):
#         r *= i
#     return r

# print(f2(5))

#neuro

def mainFunction(n1, n2):
    score = 0

    n1 = n1.lower()
    n2 = n2.lower()

    # if len(n1) == len(n2):
    #     score += 20
    print(n1[0])
    if n1[0] == 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or 'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z':
        score += 10
    else:
        return score

    if n2[0] == 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or 'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z':
        score += 10
    else:
        return score
        
    # for i in n1 and n2:
    #     if i in 'l' or 'o' or 'v' or 'e':
    #         score += 7
    #     if i in 'a' or 'e' or 'i' or 'o' or 'u':
    #         score += 12

    # for i in n2:
    #     if i in 'l' or 'o' or 'v' or 'e':
    #         score += 7
    #     if i in 'a' or 'e' or 'i' or 'o' or 'u':
    #         score += 12
    # return score
    
print(mainFunction("Alice", "Steve"))