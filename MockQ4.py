def f(L):
    X = (x for x in L for y in L if x+y == 10)
    if(len(X)>0):
        print(True)
    else:
        print(False)

# Problem 1 - use of generator comprehension instead of a list comprehension, in the case of using generators we would need
# to use convert them to some other type and store it (generators is a function that can be iterated, but does not keep
# values )
# Problem 2 - should be fruitful function, but no return statements used

# Correction
def f(L):
    X = [x for x in L for y in L if x+y == 10]
    if(len(X)>0):
        return(True)
    else:
        return(False)