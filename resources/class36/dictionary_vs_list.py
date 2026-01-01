# Run an experiment demonstrating that dictionary key lookups are much more efficient
# than list item lookups.
# Author: John MacCormick
# Date: 11/8/2023

import random
import time


def lookup(data, target):
    """The data parameter could be a list or a dictionary. Return True if the float
    value target is an element of the list or a key in the dictionary,
    otherwise return False."""
    if target in data:
        return True
    else:
        return False


def do_many_lookups(data, num_lookups):
    """The data parameter could be a list or a dictionary, containing floats as items
    or keys respectively. We look up random float values in the data, and the
    parameter num_lookups specifies how many lookups to perform."""
    for i in range(num_lookups):
        target = random.random()
        lookup(data, target)


def compare_dict_and_list():
    """Compare the time to do a large number of lookups in a very large list and a very
    large dictionary."""
    num_items = 100000  # The number of items to be stored in the list and dictionary.
    num_lookups = 10000  # The number of times to look up a random target in the list or
    # dictionary.
    big_list = []
    big_dictionary = {}
    # Insert random float values into the list and dictionary.
    for i in range(num_items):
        x = random.random()  # random float between 0.0 and 1.0
        big_list.append(x)
        big_dictionary[x] = 1  # The value in the key-value pair is irrelevant for
        # this experiment. We use 1 as the value for all keys.

    ################################################
    # Step 1. Run a timed experiment on the list.
    start = time.time()
    do_many_lookups(big_list, num_lookups)
    stop = time.time()
    list_duration = stop - start
    print('The list took', list_duration, 'seconds to do', num_lookups, 'lookups.')
    ################################################

    ################################################
    # Step 2. Run a timed experiment on the dictionary.
    start = time.time()
    do_many_lookups(big_dictionary, num_lookups)
    stop = time.time()
    dictionary_duration = stop - start
    print('The dictionary took', dictionary_duration, 'seconds to do', num_lookups,
          'lookups.')
    ################################################

    ################################################
    # Step 3. Compare performance of the list and dictionary.
    speedup = list_duration / dictionary_duration
    print('The dictionary was', speedup, 'times faster than the list.')
    ################################################


compare_dict_and_list()
