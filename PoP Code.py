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
