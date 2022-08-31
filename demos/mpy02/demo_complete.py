__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"

# this file contains all the code from the slides already typed in. it is
# suggested that you use it as a reference and instead start by viewing
# demo_template.py.

################################################################################
# Pickle
# new topics: pickle (dump, load), with, open, as
import pickle

proteins = {"1ASU": 162, "2MSI": 66, "7Q3V": 264}

filename = "prot_len.pickle"
with open(filename, "wb") as outfile:
    pickle.dump(proteins, outfile)

with open(filename, "rb") as infile:
    prot_len_new = pickle.load(infile)

print(str(proteins))
print(str(prot_len_new))


################################################################################
# Instrumentation in Python
# new topics: datetime, f-strings, str

import datetime


# simple way: add a statement
def process_transaction(sender, receiver, amount):
    write_to_log(f'process_transaction: {sender}, {receiver}, {amount}')

    # real code for processing transaction would go here.


def write_to_log(text):
    # dummy implementation for example.
    print(str(datetime.now()), text)

"""
# BONUS: dynamic way (showing off!)
_print = print


def print_instrumented(*args):
    write_to_log(str(*args))
    _print(*args)

print = print_instrumented


def display_info(id, data):
    # dummy implementation for example.
    print(data[id])
"""


################################################################################
# Decorators (#2)
# new topics: @, *

# a "decorator" function
def logged(function):

    def _decorator(*args):
        print("Logged call:", function.__name__)
        return function(*args)

    return _decorator


@logged
def dec_plain_func3():
    print("doing some stuff")


@logged
def dec_plain_func4(a, b):
    print("doing more stuff:", str(a + b))


dec_plain_func3()
dec_plain_func4(40, 2)
