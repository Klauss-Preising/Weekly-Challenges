import math

"""
First Coding Challenge:
Keeping it simple for the first one
Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. 
Compute the result recursively and another solution with loop(s).
"""


def factorial_recursion(n):
    Error_Message = "Try using a positive number."
    if n==0:
        return 1
    elif n<0:
        return Error_Message
    else:
        return n * factorial_recursion(n-1)


factorial_recursion(-5)
factorial_recursion(1)
factorial_recursion(5)


def factorial_loop(n):
    factorial = 1
    Error_Message = "Try using a positive number."
    if n==0:
        return 1
    elif n<0:
        return Error_Message
    else:
        for i in range(n,0,-1):
            factorial = factorial * i
        return factorial


factorial_loop(-5)
factorial_loop(0) 
factorial_loop(1)
factorial_loop(5)


def factorial_easy(n):
    return math.factorial(n)


factorial_loop(-5)
factorial_easy(0)
factorial_easy(1)
factorial_easy(5)