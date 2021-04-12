# Author: Corey McFarland
# Date: 01/11/2021

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
        insert_sort(test)

    with open("insert.out", "w") as out:
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
