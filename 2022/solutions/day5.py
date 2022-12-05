def parseData(data):
    return parseStacks(data[:data.index('')]), data[data.index('')+1:]

def getStackElement(row, stackNumber):
    return row[4*stackNumber - 3]

def parseStacks(unparsedStacks):
    numberOfStacks = int(unparsedStacks[-1][-2])

    stacks = []
    [stacks.append([]) for _ in range(numberOfStacks)]
        
    for row in unparsedStacks[:-1]:
        for i in range(1, numberOfStacks+1):
            element = getStackElement(row, i)
            stacks[i-1].append(element) if element != ' ' else None
    return [stack[::-1] for stack in stacks]

def parseMove(move):
    return [int(m) for m in move.replace('move ', '').replace(' from ', '//').replace(' to ', '//').split('//')]

def moveCrates9000(stacks, source, target, numberOfCrates):
    return [stacks[target-1].append(stacks[source-1].pop()) for _ in range(numberOfCrates)] 

def moveCrates9001(stacks, source, target, numberOfCrates):
    stacks[target-1] += stacks[source-1][-numberOfCrates:]
    [stacks[source-1].pop() for _ in range(numberOfCrates)]
    return stacks

def part1(data):
    stacks, moves = parseData(data)

    [moveCrates9000(stacks, sourceStack, targetStack, numberOfMoves) for numberOfMoves, sourceStack, targetStack in [parseMove(move) for move in moves]]

    return ''.join([stack[-1] for stack in stacks])

def part2(data):
    stacks, moves = parseData(data)

    [moveCrates9001(stacks, sourceStack, targetStack, numberOfMoves) for numberOfMoves, sourceStack, targetStack in [parseMove(move) for move in moves]]

    return ''.join([stack[-1] for stack in stacks])