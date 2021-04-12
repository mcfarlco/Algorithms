# Author: Corey McFarland
# Date: 01/11/2021

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

    list_quantity = 5000
    list_plot = []
    time_plot = []

    print(list_quantity)

    while list_quantity <= 35000:

        # Generate random list
        test_list = []
        for rand_int in range(0, list_quantity):
            test_list.append(random.randint(-10000, 10000))

        # Plot time to execute first sort function
        time_plot.append(sort_func(test_list))

        # Plot list quantity
        list_plot.append(list_quantity)

        # Update list quantity
        list_quantity += 5000

    with open("insertTimePlot.csv", "w") as out:
        for e in range(len(time_plot)):
            out.write(str(list_plot[e]) + "," + str(time_plot[e]))
            out.write("\n")


@sort_timer
def insert_sort(array):
    """ Function to sort a provided array using the insertion method."""

    # For arrays of length 1
    if len(array) <= 1:
        return array

    # Otherwise sort
    for index in range(1, len(array)):
        value = array[index]
        p = index - 1
        while p >= 0 and array[p] > value:
            array[p + 1] = array[p]
            p -= 1
        array[p + 1] = value


if __name__ == '__main__':
    test_sort(insert_sort)
