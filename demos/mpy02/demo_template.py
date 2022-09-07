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
# CSV (table data)
# new topics: next, str, float, strptime
import csv
import datetime
filename_csv_nice = "format_example_csv_nice.csv"
filename_csv = "format_example_csv.csv"

with open(filename_csv_nice) as csvfile:
    # TODO
    pass

with open(filename_csv) as csvfile:
    # TODO
    pass


################################################################################
# YAML (tree data)
# new topics: yaml.load, loop on dict
import yaml

filename_yaml = "format_example_yaml.yml"
with open(filename_yaml) as yamlfile:
    # TODO
    pass


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
