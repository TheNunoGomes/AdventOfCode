def getCycles(data):
    cycles = []
    for instruction in data:
        cycles.append(0)
        if instruction.startswith('addx '):
            cycles.append(int(instruction[5:]))
    return cycles

def getSignalStrengthDuringCycle(cycles, cycleNumber):
    return (1 + sum(cycles[0:cycleNumber - 1])) * cycleNumber

def getMultipleSignalStrengths(cycles, cycleNumbers):
    return [getSignalStrengthDuringCycle(cycles, cycleNumber) for cycleNumber in cycleNumbers]

def getSpritePositionDuringCycle(cycles, cycleNumber):
    return 1 + sum(cycles[0:cycleNumber - 1])

def part1(data):
    cycles = getCycles(data)
    return sum(getMultipleSignalStrengths(cycles, [20, 60, 100, 140, 180, 220]))
    

def part2(data):
    cycles = getCycles(data)
    string = ''
    pixelIndex = 1
    for i, signalChange in enumerate(cycles, 1):
        spritePosition = getSpritePositionDuringCycle(cycles, i)
        x = [p for p in range(spritePosition, spritePosition + 3)]
        string += '#' if pixelIndex in [p for p in range(spritePosition, spritePosition + 3)] else '.'
        pixelIndex += 1
        if i % 40 == 0:
            string += '\n'
            pixelIndex = 1

    return string
    