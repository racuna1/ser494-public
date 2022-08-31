__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"

################################################################################
# Instrumentation in Python
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
# Decorators