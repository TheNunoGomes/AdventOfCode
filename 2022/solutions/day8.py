def parseForestMap(data):
    return [[int(height) for height in line] for line in data]

def getTreesAbove(forestMap, treeX, treeY):
    return [int(forestMap[y][treeX]) for y in range(len(forestMap)) if y < treeY]

def getTreesBelow(forestMap, treeX, treeY):
    return [int(forestMap[y][treeX]) for y in range(len(forestMap)) if y > treeY]

def getTreesLeft(forestMap, treeX, treeY):
    return [int(height) for height in forestMap[treeY][:treeX]]

def getTreesRight(forestMap, treeX, treeY):
    return [int(height) for height in forestMap[treeY][treeX+1:]]


def isTreeVisible(forestMap, x, y):
    if x == 0 or x == len(forestMap[0]) - 1 or y == 0 or y == len(forestMap) - 1:
        return True

    treeHeight = forestMap[y][x]

    if max(getTreesAbove(forestMap, x, y)) < treeHeight:
        return True
    if max(getTreesBelow(forestMap, x, y)) < treeHeight:
        return True
    if max(getTreesLeft(forestMap, x, y)) < treeHeight:
        return True
    if max(getTreesRight(forestMap, x, y)) < treeHeight:
        return True

    return False

def getScenicScoreAbove(treesAbove, houseHeight):    
    for treeDistance, treeHeight in enumerate(treesAbove[::-1], 1): 
        if treeHeight >= houseHeight:
            return treeDistance
    return len(treesAbove)
    
def getScenicScoreBelow(treesBelow, houseHeight):
    for treeDistance, treeHeight in enumerate(treesBelow, 1):
        if treeHeight >= houseHeight:
            return treeDistance
    return len(treesBelow)
    
def getScenicScoreLeft(treesLeft, houseHeight):
    for treeDistance, treeHeight in enumerate(treesLeft[::-1], 1):        
        if treeHeight >= houseHeight:
            return treeDistance
    return len(treesLeft)
    
def getScenicScoreRight(treesRight, houseHeight):    
    for treeDistance, treeHeight in enumerate(treesRight, 1):
        if treeHeight >= houseHeight:
            return treeDistance
    return len(treesRight)

def getScenicScore(forestMap, x, y):
    if x == 0 or x == len(forestMap[0]) - 1 or y == 0 or y == len(forestMap) - 1:
        return 0

    treeHeight = forestMap[y][x]

    scenicScoreAbove = getScenicScoreAbove(getTreesAbove(forestMap, x, y), treeHeight)
    scenicScoreBelow = getScenicScoreBelow(getTreesBelow(forestMap, x, y), treeHeight)
    scenicScoreRight = getScenicScoreRight(getTreesRight(forestMap, x, y), treeHeight)
    scenicScoreLeft = getScenicScoreLeft(getTreesLeft(forestMap, x, y), treeHeight)
    
    return scenicScoreAbove * scenicScoreBelow * scenicScoreRight * scenicScoreLeft

def part1(data):
    forestMap = parseForestMap(data)
    return len([1 for y, row in enumerate(forestMap) for x in range(len(row)) if isTreeVisible(forestMap, x, y)])

def part2(data):
    forestMap = parseForestMap(data)
    return max([getScenicScore(forestMap, x, y) for y in range(len(forestMap)) for x in range(len(forestMap[0]))])