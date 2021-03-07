# Author: Corey McFarland
# Date: 02/01/2021
# Desc: HW4

def last_start(activities):
    """Function to return an array of the maximum number of activities able to schedule using a greedy algorithm
     selected by latest start time."""

    selected = []
    output = []

    # Check if array needs to be ordered
    if len(activities) <= 1:
        return activities

    # Starting from the end of the provided array
    for a in range(len(activities) - 1, -1, -1):
        if len(selected) == 0:
            index = 0

        else:
            index = len(selected) - 1

        # Check if selected activities array is empty
        # or if activity under examination ends before or when the most recently selected activity starts
        if len(selected) == 0 or activities[a][2] <= selected[index][1]:
            selected.append(activities[a])
            results.insert(0, activities[a][0])

    return output


if __name__ == '__main__':
    with open("act.txt", "r") as inp:

        # Format input into sorted iterable arrays
        results = []

        lines = inp.readlines()
        lines = [s.strip('\n') for s in lines]

        tests = int(lines[0])
        lines = lines[1:]

        while tests > 0:

            acts = []

            act_count = int(lines[0])
            lines = lines[1:]

            # Add activities to array
            for activity in range(act_count):
                temp = lines[0].split()
                act = []
                for e in temp:
                    act.append(int(e))

                # insert activities in ascending order by finish time
                if len(acts) == 0:
                    acts.append(act)

                else:
                    length = len(acts)

                    for i in range(length):
                        if int(temp[2]) < acts[i][2]:
                            acts.insert(i, act)
                            break

                        if i == len(acts) - 1:
                            acts.append(act)

                lines = lines[1:]

            results.append(last_start(acts))

            tests -= 1

        # Output results to terminal
        oi = 1
        for result in results:
            print("Set " + str(oi))
            oi += 1
            print("Number of activities selected = " + str(len(result)))
            ro = "Activities "
            for act in result:
                ro += str(act) + " "
            print(ro)
