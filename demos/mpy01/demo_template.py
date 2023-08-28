from functools import reduce

__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"

# this file contains an outline for the code demonstrations in the slides. it is
# suggested that you load up this file at the start of lecture and then fill it
# out as the lecture progresses. use it to play with the specific features we
# discuss. this file is NOT graded.


# not part of class examples. don't do this at home.
_print = print
def mp(*args):
    if "Here" in globals():
        _print(*args)
print = mp

################################################################################
# Overview
################################################################################

# only print statements after the following line will print. any above are
# skipped. it can be moved to help you focus on the code as you work down.
Here = True


# START: sample code modified from https://realpython.com/java-vs-python/
def parity(number):
    result = "odd"
    if number % 2 == 0:
        result = "even"
    return result


if __name__ == '__main__':
    for num in range(4):
        print("Number", num, "is", parity(num))

    print("Outside of loop.")
# END: sample code modified from https://realpython.com/java-vs-python/

################################################################################
# looping structures
print("==LOOPING STRUCTURES==")

lst1 = [1, 2, 3, 4]  # a list. to be discussed.

# TODO

################################################################################
# Algorithm: Linear Search
# new topics: booleans, break, pass, in


def linear_search(target, collection):
    found = False

    for item in collection:
        if item == target:
            found = True
            break
        else:
            pass  # don't actually write code like this.
    return found

# TODO


lst1 = [1, 2, 3, 4]
print(linear_search(3, lst1))
print(linear_search(10, lst1))

################################################################################
# random number generation
# new topics: modules, as, comments, docstring, randint, default args

print("==RANDOM NUMBER GENERATION==")
# the import should be at the very top.
import random
# import random as rand  #what does this do?

# TODO

################################################################################
# A DYNAMIC LANGUAGE
################################################################################

################################################################################
# dynamic typing
print("==DYNAMIC TYPING==")
lst_mixed = [10, "test", True, 5]


def func1(a, b):
    return a + b

# TODO

################################################################################
# DATA STRUCTURES
################################################################################

################################################################################
# lists
print("==LISTS==")
lst = list(["a", "b", "c"])

# TODO

################################################################################
# tuples
print("==TUPLES==")
tp = ("a", "b", "c")

# TODO

################################################################################
# list comprehension
print("==LIST COMPREHENSION==")

data1 = [3, 4, 1, 2, 6]

# TODO

################################################################################
# dictionary
print("==DICTIONARY==")
test = dict()

# TODO

################################################################################
# sets (bonus: not mentioned in lecture)
print("==SETS==")
s = set(["a", "b"])

# TODO

################################################################################
# HIGHER ORDER PROGRAMMING
################################################################################


################################################################################
# higher-order functions

def first(x):
    return x[0]


def second(x):
    return x[1]


scratch = [("Java", 0), ("LISP", 10), ("Python", 4), ("C", 3), ("JavaScript", 2)]

# TODO

################################################################################
# higher-order functions (pt2)


# a function that builds incrementor functions
def inc_maker(inc):
    def tmp(x):
        return x + inc
    return tmp


# TODO

################################################################################
# anonymous functions

# TODO

################################################################################
# map/filter/reduce


def sq(x):
    return x * x


def odd(x):
    return x % 2


def bigger(a, b):
    if b > a:
        return b
    else:
        return a


samples = [3, 4, 1, 2, 6]

# TODO

################################################################################
# UNUSED
################################################################################
