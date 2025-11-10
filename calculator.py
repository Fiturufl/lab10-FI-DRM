"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a
def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise ValueError("Base must be positive")
def exp(a, b):
    return a ** b



import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a <= 0:
        raise ValueError("Input must be positive")
    if b <= 0 or b == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(a, b)

def exp(a, b):
    return a ** b
