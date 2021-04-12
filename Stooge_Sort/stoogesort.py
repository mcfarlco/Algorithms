# Author: Corey McFarland
# Date: 01/18/2021

import math
import time
import random
import functools


def sort_timer(func):
    """
    Decorator function to track the time to execute the insert sort function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        print(time_elapsed)
        return time_elapsed
    return wrapper


def test_sort(sort_func):
    """
    Function to compare time elapsed for two sort functions for randomly generated list.
    """

    list_quantity = 500
    list_plot = []
    time_plot = []

    print(list_quantity)

    while list_quantity <= 3500:

        # Generate random list
        test_list = []
        for rand_int in range(0, list_quantity):
            test_list.append(random.randint(-10000, 10000))

        # Plot time to execute first sort function
        time_plot.append(sort_func(test_list))

        # Plot list quantity
        list_plot.append(list_quantity)

        # Update list quantity
        list_quantity += 500

    with open("stoogeTimePlot.csv", "w") as out:
        for e in range(len(time_plot)):
            out.write(str(list_plot[e]) + "," + str(time_plot[e]))
            out.write("\n")


def stooge_sort(array):
    """ Function to sort a provided array using the stooge method."""

    # For arrays of length 1
    if len(array) <= 1:
        return array

    # For arrays of length 2
    if len(array) == 2:
        if array[0] > array[1]:
            temp = array[0]
            array[0] = array[1]
            array[1] = temp

        return array

    # For arrays of length 3+
    temp_a = array
    m = math.ceil(2 * len(temp_a) / 3)
    array[:m] = stooge_sort(temp_a[:m])
    array[len(array) - m:] = stooge_sort(temp_a[len(temp_a) - m:])
    array[:m] = stooge_sort(temp_a[:m])

    return array


@sort_timer
def stooge_func(array):
    """Helper function to get overall runtime"""

    stooge_sort(array)


if __name__ == '__main__':
    test_sort(stooge_func)
