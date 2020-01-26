#Week 1
"""
Question 2
Let’s start working with some basic programs...
Write a program to print the maximum between two numbers. Create a
function e.g. maxOfTwo().
* Prompt the user for data.
"""

def maxOfTwo (a, b):
    if a > b:
        return a
    else:
        return b

"""
Question 3
Write a program to print the maximum between three integers
Hint: Try to use the maxOfTwo? (from question 2).
"""
def maxofThree(a, b, c):
    if maxOfTwo(a, b) == a and maxOfTwo(a, c) == a:
        return a
    elif maxOfTwo(a, b) == b and maxOfTwo(b, c) == b:
        return b
    else:
        return c

"""
Question 4
Write a program to identify if a number is even or odd
* Prompt the user for data.
"""

def is_even(a):
    return (a % 2 == 0)