# Week 01 - Basics
# Week 02 - Program control
# Newton's method to compute square roots:
number = 5
square = 4
while True:
    print(square)
    y = (square + number / square) / 2
    if y == square:
        break
    square = y

# Week 03 - Collections
# Mark cells in the board - tuples
boardsize = int(input("Enter size of board: "))
board = set()  # start with empty board
game_ended = False
while not game_ended:
    list_tuples = []
    listvalues = input("Enter cells to mark: ").split()
    for v in listvalues:
        value = v.split(",")
        input_tuple = (value[0], value[1])  # convert to tuple
        list_tuples.append(input_tuple)
    set_tuples = set(list_tuples)
    if len(board & set_tuples) == 0:  # empty set
        board |= set_tuples
    else:
        board -= (board & set_tuples)
    if len(board) == 0:
        print("NONE")
        game_ended = True
    elif len(board) == boardsize ** 2:
        print("ALL")
        game_ended = True

# Two sequences, print numbers from input1 that sums up = 10 with some numbers in input2 - lists
input1 = input().split()
input2 = input().split()
result = []
for i in input1:
    for j in input2:
        if (int(i) + int(j)) == 10:
            result += i
result.sort()
for i in result:
    print(i, end=" ")
print(*result)

# Seat plan - dictionaries
seatplan = {}
while True:
    reserve = input()
    if reserve == "END":
        break
    lastspace = reserve.rfind(" ")
    name = reserve[:lastspace]
    seat = reserve[lastspace + 1:]
    if seat in seatplan.values():
        print("Seat already reserved!")
    else:
        seatplan[name] = seat
for x in seatplan:
    print(x, seatplan.get(x))


# Week 04 - Memory and References
# Week 05 - Recursion


def digits_sum(n):
    if n < 10:
        return n
    else:
        last = n % 10
        other = digits_sum(n // 10)
        return last + other


def mystery_function(i, lst):
    if i == len(lst) - 1:
        return lst[i]
    else:
        mystery_variable = mystery_function(i + 1, lst)
        if lst[i] > mystery_variable:
            return lst[i]
        else:
            return mystery_variable


def vector_map(M, v, n):
    u = []  # vector represented as a list - fruitful version
    for i in range(n):
        u.append(0)
        for j in range(n):
            u[i] += M[i][j] * v[j]
    return u


def vector_map_nonfruitful(M, v, n):
    vector_copy = v.copy()
    for i in range(n):
        v[i] = 0
        for j in range(n):
            v[i] += M[i][j] * vector_copy[j]


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Week 06 - I/O and exceptions


file_name = input("Enter name of the file to read: ")
try:
    infile = open(file_name, "r")
    line = infile.readline()
    while line != '':
        print(line.rstrip())
        line = infile.readline()
except FileNotFoundError:
    print('The file does not exist!')

try:
    n = float(input("Enter a number: "))
    m = n ** 0.5
    print("Square root of this number is", m)
except Exception as e:
    print("Your number is not correct. Here are more details: ", e)


# Week 07 - OOP

# Simple clas
class Vector3d:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def scale_update(self, c):
        self._x *= c
        self._y *= c
        self._z *= c

    def dist_to(self, other):
        return ((self._x - other._x) ** 2 +
                (self._y - other._y) ** 2 +
                (self._z - other._z) ** 2) ** 0.5

    def add(self, other):
        return Vector3d(self._x + other._x,
                        self._y + other._y,
                        self._z + other._z)

    def map_update(self, M):
        vector = [0, 0, 0]
        for i in range(3):
            vector[i] = M[i][0] * self._x + M[i][1] * self._y + \
                        M[i][2] * self._z
        self._x, self._y, self._z = vector[0], vector[1], vector[2]

# Inheritance


class Shape:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def shift(self, x, y):
        self._x += x
        self._y += y

    def aligned(self, shape):
        if self._x == shape._x and self._y == shape._y:
            return True
        else:
            return False

    def has_area(self):
        return False


class Rectangle(Shape):
    def __init__(self, x, y, sideXlen, sideYlen):
        self._sideXlen = sideXlen
        self._sideYlen = sideYlen
        super().__init__(x, y)

    def has_area(self):
        return True

    def area(self):
        return (self._sideXlen * self._sideYlen)


class Square(Rectangle):
    def __init__(self, x, y, lenSide):
        super().__init__(x, y, lenSide, lenSide)


class Circle(Shape):
    def __init__(self, x, y, radius):
        self._radius = radius
        super().__init__(x, y)

    def has_area(self):
        return True

    def area(self):
        return self._radius ** 2 * 3.14

# Week 10 - Functional programming


import itertools


def my_enumerate(collection, start = 0):
    counter = itertools.count(start)
    return [(next(counter),i) for i in collection]


def binary_zip(collection1, collection2):
    it1 = iter(collection1)
    it2 = iter(collection2)
    return [(next(it1), next(it2)) for i in range(min(len(collection1), len(collection2)))]

def my_filter(function, collection):
    return [i for i in collection if function(i)]


def filteroutVowels(inChar):
    vowels = ['a','e','i','o','u']
    if(inChar in vowels):
        return False
    else:
        return True

# Higher order functions


def double(x):
    return 2*x


def square(x):
    return x*x

def sum_function_vector(f, X):
    sum = 0
    for x in X:
        sum+= f(x)
    return sum

Y = [1,2,3,4]
s1 = sum_function_vector(double, Y)
s2 = sum_function_vector(square, Y)


# Week 11 - Data structures

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Practical Mock Paper
# Q1 Implement a function
# number_of_differences(n, m, A, B)
# that takes two matrices of integers A and B with n rows and m columns and returns
# a number of positions (i, j) where an element at this position in A is not equal to
# the element at this position in B. (As usual, position (i, j) denotes i-th row and j-th
# column in the matrix.) You may assume that the matrices are of the correct size and
# are specified in a standard way as lists of lists.

def number_of_differences(n,m, A, B):
    counter = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                counter += 1
    return counter

# Q2 Implement a function
# generate_sentences(subjects, predicates, objects)
# that takes three lists of strings as parameters. The first argument is a list of words
# that can be used as a subject in a sentence, the second – as a predicate, and the third
# – as an object. The function must return a string that contains all the sentences in the
# alphabetical order that can be constructed using the provided subjects, predicates and
# objects. (Note that the words in the list of subjects are not necessarily in the alphabet-
# ical order, and the same applies to the lists of predicates and objects.) Each sentence
# must be ended by ”.” and the sentences must be separated by ” ”. (Alphabetical order
# has usual and common meaning, but if you have doubts about it, see test cases below
# for examples.)


def generate_sentences(subjects, predicates, objects):
    subjects.sort()
    predicates.sort()
    objects.sort()
    string = ""
    for s in subjects:
        for p in predicates:
            for o in objects:
                string += " " + s+" " + p + " " + o + "."
    string = string[1:]
    return(string)

# Q3 Implement a class Airplane that keeps track of the following features of an airplane:
# • consumption: an integer representing number of litres consumed per km of dis-
# tance
# • position: a tuple (pair) of integers representing a position of the plane on a map
# (assume that the airplane can only be in one of the positions of the 1 km x 1 km
# grid)
# • fuel_level: a float number representing the current fuel level in litres.
# Implement the following methods:
# • constructor __init__: takes four integer parameters (in the specified sequence)
# initX, initY, cons and init_fuel, where (initX, initY) represents initial
# location of the plane, cons represents the consumption (litre/km) and init_fuel
# represents the initial fuel level
# • goto: takes two integer parameters X and Y representing the location where the
# plane needs to go to. If the airplane has enough fuel to travel there from its
# current location, the method moves it there, updates remaining fuel level, and
# returns True. Otherwise, the plain does not move and False is returned.
# • refuel: takes one integer parameter indicating how many litres of fuel are added.
# No value returned.
# Assume that the airplane travels in a direct line between two
# p positions (X1, Y 1) and
# (X2, Y 2). The distance between two locations is computed as sqrt((X2 − X1)^2 + (Y 2 − Y 1)^2)


class Airplane:
    def __init__(self, initX, initY, cons, init_fuel):
        self.initX = initX
        self.initY = initY
        self.cons = cons
        self.init_fuel = init_fuel
        self.position = [self.initX, self.initY]
        self.fuel_level = self.init_fuel

    def goto(self, X, Y):
        distance = ((X - self.initX)**2 + (Y - self.initY)**2)**0.5
        fuel_use = self.cons * distance
        if self.init_fuel >= fuel_use:
            self.init_fuel -= fuel_use
            self.position = [X, Y]
            self.fuel_level -= fuel_use
            return True
        else:
            return False

    def refuel(self, fuel_added):
        self.fuel_level += fuel_added

# Q4 Implement a function
# longest_sequence(s)
# which takes a non-empty string s containing smaller case letters only. Find the longest
# sequence where the same letter occurs continuously in s. The function must return
# a tuple (L,N) where L is the letter and N is the length of this sequence. If there are
# several letters for which the longest continuous sequence has the same length, return
# the required information for the letter that is alphabetically smallest among those (e.g.,
# among b, y, and d the smallest is b). Do not import any libraries.


# WRONG!!!
def longest_sequence(s):
    diki = {}
    s_set = set(s)
    for i in s_set:
        diki[i] = [0, False]
    for j in range(len(list(s))):
        print([s[j]][0])
        print(diki[[s[j]][0]])
        if diki[s[j]][1]:
            diki[s[j]][0] += 1
        else:
            diki[s[j-1]][0] = 0
            diki[s[j]][1] = True
    #
    # N = [-1]
    # for k, val in diki.items():
    #     if val[0] > N[0]:
    #         N = [val[0]]
    # L = []
    # for k, val in diki.items():
    #     print(k, val[0], N[0])
    #     if val[0] == N[0]:
    #         print(k, val)
    #         L += [k]
    return (diki)
            

s = "abbbadddadd"
assert longest_sequence("dghhhmhmx") == ("h", 3)
assert longest_sequence("dhkkhhkkkt") == ("k", 3)
assert longest_sequence("abbbadddadd") == ("b", 3)

# Mock paper 2018

# Q1
# The Fibonacci series starts with 0, 1, . . .; each term is the sum of the two previous
# terms. For example,
# 0 1 1 2 3 5 8 13 ...
# (a) Write a Python program to print out the first 20 fibonacci numbers, each number
# separated by a space.
# (b) Write a second Python program to print out the fibonacci series, separated
# by spaces, up to, but not including, the number 2000, and then print out
# how many terms were printed.

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(20):
    print(fibo(i), end=" ", flush=True)

counter = 0
while True:
    if fibo(counter) < 2000:
        print(fibo(counter))
        counter += 1
    else:
        print(counter)
        break

# Q2
# Write a function to search a list of strings for a specified value. The function
# takes a search string, str), a list of strings (lst), and the size of the list (size),
# and returns the number of the slot that contains the search string, or returns -1
# if the search string does not appear.
# search (str, lst, size)

def search(str, lst, size):
    res = -1
    for i in range(size):
        if str == lst[i]:
            res = i
    return res


# Q3
# Write a program for a number guessing game. The program generates a random
# number between 0 and 99, and then asks the user to guess that number. For
# each guess the program replies Correct, Too low, or Too high. If the number
# is correct, the program prints the number of guesses it took. If not, the program
# asks the user to guess again. For example:
# Guess a number between 0 and 99: 50
# Too low. Guess again: 75
# Too high. Guess again: 60
# Too high. Guess again: 54
# Correct. It took you 4 guesses.
# Your program should make use of a boolean flag.

from random import randint

def game():
    n = randint(0, 99)
    guess = int(input("Guess a number between 0 and 99"))
    count = 0
    flag = True
    while flag:
        if guess < n:
            print("Too low. Guess again:")
            count += 1
            guess = int(input())
        elif guess > n:
            print("Too high. Guess again:")
            count += 1
            guess = int(input())
        else:
            print(f"Correct. It took you {count} guesses")
            flag = False

# Q4
# Write a program to score True-False tests. Correct answers get 1 point, wrong
# answers -1 point and no answer (i.e., x) gets 0. The program first reads in the
# thirty correct answers to the test questions (each answer being T or F). It then
# reads a series of answer sets – each of these is a student number (an integer)
# followed by thirty answers, each of which is one of the characters T, F, or x.
# x is used to report that no answer was given. The input is terminated by a
# record beginning with the student number 999. The program should output
# each student number followed by their score on the test.


def score(n):
    correct = input("Provide correct answer template: ")
    corr_list = correct.split()
    list = []
    for i in range(n):
        pu = input("Enter students results: ")
        index = pu.index(" ") + 1
        pu2 = pu[index:].split()
        marks = 0
        for i in range(len(corr_list)):
            if pu2[i] == "x":
                continue
            elif pu2[i] == corr_list[i]:
                marks += 1
            elif pu2[i] != corr_list[i]:
                marks -= 1
        # if marks < 0: could marks be less than 0?
        #     marks = 0
        list += [[pu[:index], f"{marks} marks"]]
    for i in list:
        print(*i)

# Mock paper 2018 Evening

# Q3
# Complete the function definition so it returns the square of the product of the
# parameters, so sqrProd(2, 5) returns (2*5)*(2*5) = 100.


def sqrProd(x, y):
    return (x*y)*(x*y)

# Q4
# A mobile telephone company offers two types of service: regular and premium.
# Its rates vary, depending on the type of service. The monthly rates are computed
# as follows:
# Regular service:
# £10.00 for the first 50 minutes. Charges for over 50
# minutes are 20 pence per minute.
# Premium service: £25.00 monthly charge plus
# a. for calls made from 6:00am to 6:00pm (daytime), the
# first 75 minutes are free; charges for over 75 minutes are
# 10 pence per minute
# b. for calls made from 6:00pm to 6:00am (off-peak), the
# first 100 minutes are free; charges for over 100 minutes
# are 5 pence per minute.
# Write a program to calculate and print mobile phone bills. The input is a series
# of records each giving the account number (a string), the customer surname, the
# balance on the account from last month, the type of service (R or P, for Regular
# or Premium, as explained below), followed by a single number of call minutes in
# the case of Regular service, and the number of daytime minutes and the number
# of off-peak minutes in the case of Premium customers.
# The file is terminated by a value of X0000 in place of an account number.

# Easy but time consuming


# Q3

s = "My name is Michele"
new_s = s.split()
new_s = new_s[::-1]
print(*new_s)

# Q4

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Q5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

[x for x in set(a) if x in b]
[x for x in set(b) if x in a]


# Q2


def power(a, n):
    if n == 1:
        return a
    else:
        return power(a, n-1)*a

# import pytest
#
# from PoPCode.py import power


# Q3

n = int(input())
#???

# Q4

n = int(input())


def test_power():
    assert power(2,3) == 8


for el in range(1, 101):
    if el % 7 != 0 and str(7) not in str(el):
        print(el)


    # MISTAKES???
"""
Question 6 from PracticalPaper3.pdf:
1256 is 1 cow, 1 bull, shouldn't it be 1 cow

"""