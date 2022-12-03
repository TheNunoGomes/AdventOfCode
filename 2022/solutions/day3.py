def splitListInHalf(list):
    halfIndex = len(list)//2
    return list[:halfIndex], list[halfIndex:]

def itemAsciiToPriority(item):
    # ASCII 'a' = 97, ASCII 'A' = 65, so we swap case
    # After swapping case, we need to offset by 65, so that 'a' (which is now 'A' with ASCII value 65) corresponds to priority 1
    value = ord(item.swapcase()) - 64
    # Lastly, we offset by 6, for ASCII characters 91-96, if we have a priority over 26, so that 'A' has priority 27
    value = value if value < 27 else value - 6
    return value


def part1(data):
    prioritySum = 0
    for rucksack in data:
        firstCompartment, secondCompartment = splitListInHalf(rucksack)
        for item in secondCompartment:
            if item in firstCompartment:
                prioritySum += itemAsciiToPriority(item)
                break

    return prioritySum

def part2(data):
    prioritySum = 0
    for i in range(0, len(data), 3):
        rucksack1, rucksack2, rucksack3 = data[i], data[i+1], data[i+2]

        for item in rucksack1:
            if item in rucksack2 and item in rucksack3:
                prioritySum += itemAsciiToPriority(item)
                break

    return prioritySum