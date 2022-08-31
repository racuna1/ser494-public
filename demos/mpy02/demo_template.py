__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"

# this file contains an outline for the code demonstrations in the slides. it is
# suggested that you load up this file at the start of lecture and then fill it
# out as the lecture progresses. use it to play with the specific features we
# discuss. this file is NOT graded.


################################################################################
# Pickle
# new topics: pickle (dump, load), with, open, as
import pickle

proteins = {"1ASU": 162, "2MSI": 66, "7Q3V": 264}

# TODO


################################################################################
# Instrumentation in Python
# new topics: datetime, f-strings, str

import datetime

# TODO


def write_to_log(text):
    # dummy implementation for example.
    print(str(datetime.now()), text)


################################################################################
# Decorators (#2)
# new topics: @, *

# a "decorator" function
def logged(function):

    def _decorator(*args):
        print("Logged call:", function.__name__)
        return function(*args)

    return _decorator

# TODO
