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
    proteins_new = pickle.load(infile)

print(str(proteins))
print(str(proteins_new))


################################################################################
# CSV (table data)
# new topics: next, str, float, strptime
import csv
import datetime
filename_csv_nice = "format_example_csv_nice.csv"
filename_csv = "format_example_csv.csv"

with open(filename_csv_nice) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)
        print(f"id: {str(row['id'])}")
        print(f"attempt: {float(row['attempt'])}")

        # '2022-09-04 11:00:00 UTC'
        time = datetime.datetime.strptime(row['submitted'], "%Y-%m-%d %H:%M:%S %Z")
        print(time)

with open(filename_csv) as csvfile:
    reader = csv.reader(csvfile)  # can't use DictReader since column titles not unique.

    header = next(reader)
    for i, title in enumerate(header):
        print(i, title)

    for row in reader:
        print(row)


################################################################################
# YAML (tree data)
# new topics: yaml.load, loop on dict
import yaml

filename_yaml = "format_example_yaml.yml"
with open(filename_yaml) as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

    for entry in data:  # data is a dict, this loops over its keys.
        cur = data[entry]  # this dict has several keys, we'll just look at one.
        print(cur[":submitters"])
        print(cur[":submitters"][0][":name"])
        print(cur[":submitters"][0][":sid"])
        print(cur[":submitters"][0][":email"])


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
