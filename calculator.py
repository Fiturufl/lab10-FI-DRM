#https://github.com/Fiturufl/lab10-FI-DRM.git
#Partner 1: Francisco Iturriaga
#Partner 2: David Reyes-Munoz
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def exp(a, b):
    return a ** b

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Input must be positive")
    if b <= 0 or b == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(a, b)
