def parseElfSections(elfPair):
    elf1, elf2 = elfPair.split(',')
    return [int(section) for section in elf1.split('-')], [int(section) for section in elf2.split('-')]

def sectionsAreFullyContained(elf1, elf2):
    return elf1[0] <= elf2[0] and elf1[1] >= elf2[1] or elf2[0] <= elf1[0] and elf2[1] >= elf1[1]

def sectionsArePartiallyContained(elf1, elf2):
    return elf1[0] >= elf2[0] and elf1[0] <= elf2[1] or elf2[0] >= elf1[0] and elf2[0] <= elf1[1]

def part1(data):
    return [sectionsAreFullyContained(e1, e2) for e1, e2 in [parseElfSections(elfPair) for elfPair in data]].count(True)

def part2(data):    
    return [sectionsArePartiallyContained(e1, e2) for e1, e2 in [parseElfSections(elfPair) for elfPair in data]].count(True)