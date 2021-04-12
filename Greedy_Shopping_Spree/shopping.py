# Author: Corey McFarland
# Date: 01/25/2021

def shopping(family, item_prices, item_weights):
    """Function to determine shopping spree items for provided family and items"""

    f_hold = []
    f_win = 0

    # Find max value and items for each family member
    for person in family:
        hold = []
        p_hold = []

        for w in range(person + 1):
            base = [0]
            hold.append(base)

        for i in range(len(item_prices)):
            for w in range(person + 1):
                if item_weights[i] <= w:
                    if item_prices[i] + hold[w-item_weights[i]][i] > hold[w][i]:
                        hold[w].append(item_prices[i] + hold[w-item_weights[i]][i])

                    else:
                        hold[w].append(hold[w][i])
                else:
                    hold[w].append(hold[w][i])

        # Add winnings to family total
        f_win += hold[person][len(item_prices)]


        # Record items to array
        p_win = hold[person][len(item_prices)]
        for i in range(len(item_prices), 0, -1):
            if p_win <= 0:
                break

            if p_win == hold[person][i - 1]:
                continue

            else:
                p_hold.append(i)

                p_win = p_win - item_prices[i - 1]
                person = person - item_weights[i - 1]

        p_hold.sort()
        f_hold.append(p_hold)

    # Format array for output
    f_hold.insert(0, f_win)

    return f_hold


if __name__ == '__main__':
    with open("shopping.txt", "r") as inp:

        results = []

        lines = inp.readlines()
        lines = [s.strip('\n') for s in lines]

        tests = int(lines[0])
        lines = lines[1:]
        print(lines)

        while tests > 0:
            family = []
            item_p = []
            item_w = []

            item_count = int(lines[0])
            lines = lines[1:]

            for item in range(item_count):
                temp = lines[0].split()
                item_p.append(int(temp[0]))
                item_w.append(int(temp[1]))
                lines = lines[1:]

            family_count = int(lines[0])
            lines = lines[1:]

            for person in range(family_count):
                family.append(int(lines[0]))
                lines = lines[1:]

            results.append(shopping(family, item_p, item_w))

            tests -= 1

        print(results)

    with open("results.txt", "w") as out:
        i = 1
        for tests in results:
            p = 1

            out.write("Test Case " + str(i) + "\n")
            out.write("Total Price " + str(tests[0]) + "\n")
            out.write("Member Items" + "\n")

            for p in range(1, len(tests)):
                out.write(str(p) + ": ")
                for item in tests[p]:
                    out.write(str(item) + " ")
                out.write("\n")

            i += 1
