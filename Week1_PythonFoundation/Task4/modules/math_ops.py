import math

def area_of_circle(radius):
    return math.pi * radius * radius

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
