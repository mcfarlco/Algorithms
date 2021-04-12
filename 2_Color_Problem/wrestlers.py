# Author: Corey McFarland
# Date: 02/15/2021

def good_bad(wrestlers, rivalries):
    """Function to determine if a 'Babyfaces' and 'Heels' split is possible from a provided list of wrestlers and
    rivalries."""

    # Team[0] = Babyfaces, Team[1] = Heels
    team = [[],[]]
    stack = []
    visited = []

    # Iterate through all unvisited vertices
    for w in wrestlers:
        if w in visited:
            continue

        # If new vertex, add to babyfaces
        team[0].append(w)
        visited.append(w)

        # Check if new vertex has one or more edges
        for r in rivalries:
            if w in r:
                for v in r:
                    if v != w:

                        # Check if adjacent vertices are in babyfaces which is a rivalry conflict.
                        if v in team[0]:
                            return ["Impossible"]

                        # Otherwise add to heels if not already there.
                        else:
                            if v in team[1]:
                                continue
                            else:
                                team[1].append(v)
                                stack.append(v)

        # Perform a BFS on the adjacent vertices
        while len(visited) < len(wrestlers) and len(stack) > 0:

            # Update stack
            cur_v = stack[0]
            if cur_v in visited:
                stack.remove(cur_v)
                continue

            # Check the team of the current vertex to determine what team to add new adjacent vertices.
            if cur_v in team[1]:
                i = 1
                j = 0

            else:
                i = 0
                j = 1

            # Add new vertex to visited
            visited.append(cur_v)

            # Check for unvisited adjacent vertices
            for r in rivalries:
                if cur_v in r:
                    for e in r:
                        if e != cur_v:

                            # Check if adjacent vertices have a rivalry conflict.
                            if e in team[i]:
                                return ["Impossible"]

                            # Otherwise add to other team if not already there.
                            else:
                                if e in team[j]:
                                    continue
                                else:
                                    team[j].append(e)
                                    stack.append(e)

    return ["Yes Possible", team[0], team[1]]


if __name__ == '__main__':

    print("Please enter the input file:")

    with open(input(), "r") as inp:

        # Format input into arrays
        wrestlers = []
        rivalries = []

        lines = inp.readlines()
        lines = [s.strip('\n') for s in lines]

        num_wres = int(lines[0])
        lines = lines[1:]

        while num_wres > 0:
            wrestlers.append(lines[0])
            lines = lines[1:]
            num_wres -= 1

        num_riv = int(lines[0])
        lines = lines[1:]

        while num_riv > 0:
            rivalries.append(lines[0].split())
            lines = lines[1:]
            num_riv -= 1

        # Check for rivalry compatibility
        result = good_bad(wrestlers, rivalries)

        # Output results to terminal
        if len(result) == 1:
            print(result[0])

        else:
            print(result[0])

            babyfaces = "Babyfaces: "
            for b in result[1]:
                babyfaces = babyfaces + b + " "
            print(babyfaces)

            heels = "Heels: "
            for h in result[2]:
                heels = heels + h + " "
            print(heels)

            print("Note: there are other possible solutions")
