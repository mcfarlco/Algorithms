# Author: Corey McFarland
# Date: 01/11/2021
# Desc: HW1 problem 4

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


if __name__ == '__main__':
    with open("data.txt", "r") as inp:
        tests = []

        # Import lines as new array to test
        for line in inp:

            # Import elements that are separated by strings as an array
            array = line.split()

            # Update array to be the number of elements to be sorted (determined by first element, which is skipped)
            for e in range(1, int(array[0]) + 1):
                array[e-1] = int(array[e])

            array = array[:e]
            tests.append(array)

    for test in tests:
        merge_sort(test)

    with open("merge.out", "w") as out:
        for array in tests:
            # Add number of elements sorted to output
            out.write(str(len(array)) + " ")

            # Add array to output, with elements separated with spaces
            for e in range (len(array)):
                out.write(str(array[e]))
                if e == len(array):
                    continue
                else:
                    out.write(" ")
            # Write a new line for each array
            out.write("\n")
