import math

def area_of_circle(radius):
    return math.pi * radius * radius

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
