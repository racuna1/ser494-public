from functools import reduce

__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"

# this file contains all the code from the slides already typed in. it is
# suggested that you use it as a reference and instead start by viewing
# demo_template.py.


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

lst1 = [1, 2, 3, 4] # a list. to be discussed.

for item in lst1:
    print(item)

for i in range(len(lst1)):
    print(lst1[i])

for item, i in enumerate(lst1):  # this is unpacking a "tuple" behind the scenes.
    print(item, i)

print("item:", item)  # "lovely" dynamic declaration

i = 0
while i < len(lst1):
    print(lst1[i])
    i += 1
    # i++ #what happens with this?

################################################################################
# A DYNAMIC LANGUAGE
################################################################################

################################################################################
# dynamic typing
print("==DYNAMIC TYPING==")
lst_mixed = [10, "test", True, 5]


def func1(a, b):
    return a + b

print(lst_mixed)
print(func1(4, 5))
print(func1("X", "Y"))


################################################################################
# DATA STRUCTURES
################################################################################

################################################################################
# lists
print("==LISTS==")
lst = list(["a", "b", "c"])

# assorted operations as examples.
lst.append("d")
lst += ["e"]
result = lst[4]
lst2 = lst[:]
lst3 = lst[::-1]
test = [None] * 5

print(len(lst))
print(result)
if "z" in lst:  # O(n)
    print("found")

################################################################################
# tuples
print("==TUPLES==")
tp = ("a", "b", "c")

# assorted operations as examples.
print(tp)
print(tp[2])
# tp[2] = 3 # what happens here?

################################################################################
# list comprehension
print("==LIST COMPREHENSION==")

data1 = [3, 4, 1, 2, 6]
data1a = [x * x for x in data1]
data1b = [x * x for x in data1 if x % 2 == 0]
data1c = [(x, x + 1) for x in data1]
print(data1a)
print(data1b)
print(data1c)

# doesn't really fit here but oh well.
lst1 = [0] * 5
print(lst1)

################################################################################
# dictionary
print("==DICTIONARY==")
test = dict()

# assorted operations as examples.
test[240] = 5
# test[lst] = 34 # what happens here?
test[tp] = 34
test[240] += 10

print(test.keys())
print(test[240])

# slightly longer example
freq = dict()

for x in "CATACGCATGCAATACGG":
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print(freq)

################################################################################
# sets (bonus: not mentioned in lecture)
print("==SETS==")
s = set(["a", "b"])

# assorted operations as examples.
s.add("a")
s.add("c")
s.remove("b")
# union and intersection are also available.
# x.union(y)
# x.intersection(y)

if "z" in s:  # O(1) :clapping:
    print("found")

print(s)

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

print(sorted(scratch, key=first))
print(sorted(scratch, key=second))

################################################################################
# higher-order functions (pt2)


# a function that builds incrementor functions
def inc_maker(inc):
    def tmp(x):
        return x + inc
    return tmp


inc5 = inc_maker(5)
inc10 = inc_maker(10)

print(inc5(100))
print(inc10(100))

################################################################################
# anonymous functions
print((lambda x: x * x * x)(3))
cube = lambda x: x * x * x
print(cube(3))

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

samples_a = list(map(lambda x: x * x, samples))
samples_b = [x * x for x in samples]
samples_c = [sq(x) for x in samples]

samples_filtered_a = list(filter(lambda x: x % 2, samples))
samples_filtered_b = [x for x in samples if x % 2]
samples_filtered_c = [x for x in samples if odd(x)]

largest = reduce(bigger, samples)

mymax = lambda lt: reduce(bigger, lt)
print(mymax(samples))

################################################################################
# UNUSED
################################################################################
