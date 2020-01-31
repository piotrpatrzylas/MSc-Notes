#Week 1
"""
Question 2
Let’s start working with some basic programs...
Write a program to print the maximum between two numbers. Create a
function e.g. maxOfTwo().
"""
def maxOfTwo (a, b):
    if a > b:
        return a
    else:
        return b
"""
Question 3
Write a program to print the maximum between three integers
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
"""
def is_even(a):
    return (a % 2 == 0)
"""
Question 5
Create the following list of names Juliet, John, Jack, Joy, Jim, Josh, Julia and
prompt the user to enter for a name.
Search the list if the name is matched with the names of the list and
print:
“name found it” if there is a match.
“name not found” in any other case
* Output Example: “Sara found it!”
"""
q5l = ["Juliet", "John", "Jack", "Joy", "Jim", "Josh", "Julia"]
q5inp = input("Enter name: ")
if q5inp in q5l:
    print("Found")
else:
    print("Not found")
"""
Question 6
Create a function to return the average of three or the sum of three depending
on the user selection.
*Hint! : The user will enter 4 parameters, e.g. “avg_of_3” for average,
“sum_of_3” for sum and three numbers.
"""
def avg_sum_of_3(a,b,c, select):
    if select == "avg_of_3":
        return (a+b+c) / 3
    if select == "sum_of_3":
        return a+b+c
"""
Question 7
Develop four functions as example cases for the following time complexities:
o O(1)
o O(n)
o O(n 2 )
o O(n3) -> Multiply two matrices
"""
testlist = [1,2,3,4]
testlist2 = [[1,2,3],[1,2,3]]
def fun1(tlist):
    return tlist[0]
def fun2(tlist2):
    for el in tlist2:
        print (el)
def fun3(tlist3):
    sum = 0
    for el in tlist3:
        for el2 in el:
            sum += el2
    print(sum)

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
def fun4(tl1, tl2):
    first = len(X)
    second = len(Y[0])
    results = [[0]*second]*first
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                results[i][j] += X[i][k] * Y[k][j]
    return results
"""
Question 8
Develop the following Python functions:
1. Linear search
Given a two dimensional list of “n x m” elements, write a function to
count occurrences of a given key.
The function should also return a matrix of the position of a key in
the 2 dimensional list.
For example, given the following list:
Mylist = [[1,4,7],[4,5,2],[6,4,8]]
and a key, e.g. key = 4
The output should be
3, [[0, 1], [1, 0], [2, 1]]
# 3 occurrences of number 4 in positions: 0,1, 1,0 and 2,1
What is the complexity of the linear search in the 2 dimensional
array?
"""
# Seperete file - algorithms
"""
Homework 1
Develop BubbleSort (hint)
o It is the simplest sorting algorithm that works by repeatedly
swapping the adjacent elements if they are in wrong order.
o Implement a simple bubble sort algorithm!
o What is the complexity of Bubble sort?
"""
# Seperete file - algorithms
"""
Homework 2 (Google Interview Question)
Leetcode.com is an online tool with a collection of interview and coding
questions.
Solve the following: https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def two_sum(nums, target):
    results = []
    for i in nums:
        missing = target - i
        if missing in nums:
            results.append(nums.index(i))
            results.append(nums.index(missing))
            break
    return results
# Week2
"""
Question 1
Generate a list of 100 random numbers in ascending order.
• write a function to generate the numbers
• make sure your list is in ascending order
o without using any sort!
• consider initialization issue, and
• check that it avoids repeated values.
"""

import random
r0 = random.randint(1, 5)
l = [r0]
for i in range(99):
    new = random.randint(1, 5) + l[-1]
    l.append(new)
"""
Question 2
Develop your:
• Binary Search or Interpolation Search Python function
• Use a pseudocode from Wikipedia and come up with your version,
using a list to represent the collection A.
OR
• Download the Python version from here:
https://www.geeksforgeeks.org/binary-search/
•Use the function from Question 1 to test your Binary Search or
Interpolation Search Python function
"""
# Seperete file - algorithms
"""
Question 3
Develop a benchmark function to study differences between the recursive and
iterated versions of Binary search.
Code is available at: https://www.geeksforgeeks.org/binary-search/
• iterativeBinarySearch(arguments...)
• recursiveBinarySearch(arguments...)
Benchmark for different sizes of arrays (e.g. generate 1000, 10K, 100K, 1M size
ordered arrays).
"""

"""
Homework (or in class if you finish on time!)
Develop a code to simulate a lottery.
Create a function that generates:
• 6 numbers from a pool of numbers 1 to 49
• 1 number (Joker) from a pool of 1 to 10 numbers.
Develop a program to simulate:
• A user selection (6 numbers plus 1 Joker)
• The ball numbers (6 numbers plus 1 Joker)
The program should output:
You entered: [[11, 20, 4, 30, 44, 8], [8]]
Numbers drawn: [[33, 12, 14, 11, 29, 34], [5]]
You guessed correctly: {11}
You did not match the Joker!
Example outputs:
You entered: [[25, 22, 31, 30, 20, 5], [6]]
Numbers drawn: [[17, 1, 23, 47, 46, 12], [6]]
You guessed correctly: None!
('You matched the Joker!', {6})
You entered: [[1, 18, 9, 47, 30, 43], [10]]
Numbers drawn: [[38, 28, 24, 12, 18, 43], [7]]
You guessed correctly: {18, 43}
You did not match the Joker!
You entered: [[9, 6, 41, 12, 16, 15], [4]]
Numbers drawn: [[33, 35, 48, 17, 46, 1], [5]]
You guessed correctly: None!
You did not match the Joker!
"""
def number_gen():
    joker = random.randint(1,10)
    numbers = []
    counter = 6
    while counter > 0:
        n = random.randint(1, 49)
        if n not in numbers:
            numbers.append(n)
            counter -= 1
    lot_numbers = [numbers, [joker]]
    return lot_numbers

def lottery():
    user_sel = number_gen()
    casino_sel = number_gen()
    print("You entered ", user_sel, "\nNumbers drawn", casino_sel)
    guessed = set()
    for el in user_sel[0]:
        if el in casino_sel[0]:
            guessed.add(el)
    if len(guessed) == 0:
        print ("You guessed correctly: None!")
    else:
        print("You guessed correctly: ", guessed)
    if user_sel[1] == casino_sel[1]:
        print ('You matched the Joker!', set(user_sel[1]))
    else:
        print("You did not match the Joker!")

