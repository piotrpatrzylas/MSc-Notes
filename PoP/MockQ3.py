def add_row(A, v, n):
    A.extend([v]*n)

A = [[1, 2], [3, 4]]
v = [5, 6]
add_row(A, v, 2)
v[0] = 0
print(A)

# The problem is with the referencing. When we extend A with [V] there is only reference to the object used - [V],
# instead of copying and extending values of that object. When we later change value of V values in A will
# be also updated.

# SOLUTIONS:
# Simple version assuming [V] will be always simple (not nested) list.
def add_row(A, v, n):
    A.extend([v[:]]*n)

# Version with deepcopy for nested lists.
from copy import deepcopy

def add_row(A, v, n):
    A.extend(deepcopy([v])*n)
