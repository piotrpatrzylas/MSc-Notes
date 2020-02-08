"""
Question 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 6 marks
Implement a function
number_of_differences(n, m, A, B)
that takes two matrices of integers A and B with n rows and m columns and returns a
number of positions (i, j) where an element at this position in A is not equal to the
element at this position in B. You may assume that the matrices are of the correct size
and are specified in a standard way as lists of lists.
Indicative test cases:
assert number_of_differences(2,3, [[1,2,3], [4,5,6]], [[1,2,4],\
[3,5,6]]) == 2
assert number_of_differences(2,2, [[1,2], [3,4]], [[1,2], [3,4]])== 0
"""
la = [[1,2,3], [4,5,6]]
lb = [[1,2,4], [3,5,6]]
def number_of_differences(n, m, A, B):
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return j #which should be wrong, it is not a tuple to pass the tests...
    else:
        return 0



"""
Question 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 7 marks
Implement a function
generate_sentences(subjects, predicates, objects)
that takes three lists of strings as parameters. The first argument is a list of words
that can be used as a subject in a sentence, the second – as a predicate, and the third
– as an object. The function must return a string that contains all the sentences in
the alphabetical order that can be constructed using the provided subjects, predicates
and objects. (Note that the words in the list of subjects are not necessarily in the
alphabetical order, and the same applies to the lists of predicates and objects.) Each
sentence must be ended by ”.” and the sentences must be separated by ” ”.
Indicative test cases:
assert generate_sentences(["John", "Mary"], ["hates", "loves"],\
["apples", "bananas"])) == "John hates apples. John hates bananas. \
John loves apples. John loves bananas. Mary hates apples. \
Mary hates bananas. Mary loves apples. Mary loves bananas."
assert generate_sentences(["Vlad", "Hubie"], ["drives"],\
["car, motorcycle, bus"])) == "Hubie drives bus. Hubie drives car. \
Hubie drives motorcycle. Vlad drives bus. Vlad drives car. \
Vlad drives motorcycle."
"""
def generate_sentences(subjects, predicates, objects):
    subjects.sort()
    predicates.sort()
    objects.sort()
    sentence = ""
    slist = []
    for s in range(len(subjects)):
        for p in range(len(predicates)):
            for o in range(len(objects)):
                sentence += subjects[s] + " " + predicates[p] + " " + objects[o] + "." + " "
    sentence = sentence[:-1]
    return sentence
"""

Question 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 12 marks
Implement a class Airplane that keeps track of the following features of an airplane:
• consumption: an integer representing number of litres consumed per km of dis-
tance
• position: a tuple (pair) of integers representing a position of the plane on a map
with 1 km precision (assume that the airplane can only be in one of the positions
of the grid)
• fuel_level: a float number representing the current fuel level in litres.
Implement the following methods:
• constructor __init__: takes four integer parameters (in the specified sequence)
initX, initY, cons and init_fuel, where (initX, initY) represents initial
location of the plane, cons represents the consumption (litre/km) and init_fuel
represents the initial fuel level
• goto: takes two integer parameters X and Y representing the location where the
plane needs to go to. If the airplane has enough fuel to travel there from its
current location, the method moves it there, updates remaining fuel level, and
returns True. Otherwise, the plain does not move and False is returned.
• refuel: takes one integer parameter indicating how many litres of fuel are added.
No value returned.
Assume that the airplane travels in a direct line between two
p positions (X1, Y 1) and
(X2, Y 2). The distance between two locations is computed as (X2 − X1) 2 + (Y 2 − Y 1) 2
Indicative test cases:
ap789 = Airplane(0, 0, 10, 3000)
assert ap789.goto(95,70) == True
assert ap789.position[0] == 95 and ap789.position[1]==70
assert abs(ap789.fuel_level - 1819.96) < 0.01"""
class Airplane():
    def __init__(self, initX, initY, cons, initFuel):
        self.position = (initX, initY)
        self._cons = cons
        self.fuel_level = initFuel
    def goto(self, x, y):
        self.newposition = (x,y)
        self.distance = ((self.position[0]-self.newposition[0])**2 +\
                        (self.position[1]-self.newposition[1])**2)**0.5
        self.maxDist = self.fuel_level / self._cons
        self.fused = self.distance * self._cons
        self.canGo = False
        if self.maxDist >= self.distance:
            self.canGo = True
            self.position = self.newposition
            self.fuel_level -= self.fused
        return self.canGo
    def refuel(self, fadded):
        self.fuel_level += fadded

"""
Question 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 15 marks
Implement a function
longest_sequence(s)
which takes a non-empty string s containing smaller case letters only. Find the longest
sequence where the same letter occurs continuously in s. The function must return a
tuple (L,N) where L is the letter and N is the length of this longest sequence. If there
are several letters for which the longest continuous sequence has the same length, print
the required information for the smallest (alphabetically) letter. Do not import any
libraries.
Indicative test cases:
assert longest_sequence("dghhhmhmx") == ("h", 3)
assert longest_sequence("dhkkhhkkkt") == ("k", 3)
assert longest_sequence("abbbadddadd") == ("b", 3)
"""

def longest_sequence(s):
    dict = {}
    letters = set(s)
    for i in letters:
        dict.update({i: 0})
    currentStreak = 1
    first = s[0]
    streak = 0
    for i in range(1, len(s)):
        if s[i] == first:
            streak += 1
        first = s[i]
s = 'dghhhmhmx'
longest_sequence(s)

