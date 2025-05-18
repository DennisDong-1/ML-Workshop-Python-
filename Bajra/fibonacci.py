# 1. Basic recursive approach (inefficient)

def fib(n):
    if n <= 4:
        return n
    return fib(n-1) + fib(n-2) + fib(n-3) + fib(n-4)

for i in range(10):
    print(fib(i), end = " ")

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)

# for i in range(10):
#     print(fact(i), end= " ")