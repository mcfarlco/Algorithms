# Author: Corey McFarland
# Date: 01/11/2021
# Desc: HW1 problem 5a

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

    while list_quantity <= 35000:

        print(list_quantity)

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

    with open("mergeTimePlot.csv", "w") as out:
        for e in range(len(time_plot)):
            out.write(str(list_plot[e]) + "," + str(time_plot[e]))
            out.write("\n")


def merge(left, right):
    """Function to two merge arrays in ascending order"""

    # If only one value in one of the arrays, return that array
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    temp = []
    li = 0
    ri = 0

    while len(temp) < len(left) + len(right):
        if li == len(left) and ri < len(right):
            temp.append(right[ri])
            ri += 1

        elif ri == len(right) and li < len(left):
            temp.append(left[li])
            li += 1

        elif left[li] < right[ri]:
            temp.append(left[li])
            li += 1

        else:
            temp.append(right[ri])
            ri += 1

    return temp


def merge_sort(array):
    """ Function to sort a provided array using the merge method."""

    # For arrays of length 1
    if len(array) <= 1:
        return array

    # Otherwise recursively sort the half and merge
    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])
    t = merge(left, right)

    # Update array
    for e in range(len(array)):
        array[e] = t[e]
    return array

@sort_timer
def merge_func(array):
    merge_sort(array)


if __name__ == '__main__':
    test_sort(merge_func)
