def getAdjacent(data, row, col):
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[row]):
        return []
    adjacent = []
    if row > 0:
        adjacent.append(data[row-1][col])
    if col > 0:
        adjacent.append(data[row][col-1])
    if col < len(data[row])-1:
        adjacent.append(data[row][col+1])
    if row < len(data)-1:
        adjacent.append(data[row+1][col])
    return adjacent

def measureBasin(data, row, col, size, scannedPositions):
    if row < 0 or row >= len(data) or col < 0 or col >= len(data[row]) or data[row][col] == '9':
        return -1
    if [row, col] in scannedPositions:
        return 0
    else:
        scannedPositions.append([row, col])

    data[row] = f"{data[row][:col]}9{data[row][col+1:]}"
    if row > 0 and data[row-1][col] != '9':
        measureBasin(data, row-1, col, size+1, scannedPositions)
    if col > 0 and data[row][col-1] != '9':
        measureBasin(data, row, col-1, size+1, scannedPositions)
    if col < len(data[row])-1 and data[row][col+1] != '9':
        measureBasin(data, row, col+1, size+1, scannedPositions)
    if row < len(data)-1 and data[row+1][col] != '9':
        measureBasin(data, row+1, col, size+1, scannedPositions)
        
    return len(scannedPositions)

def sumLowPointRisks(data):
    total = 0
    for i, heightmap in enumerate(data):
        for j, height in enumerate(heightmap):
            if height == '9':
                continue
            if len([a for a in getAdjacent(data, i, j) if int(a) <= int(height)]) == 0:
                total += int(height) + 1
    return total

def multiplyThreeLargestBasins(data):
    largestBasinSizes = [0, 0, 0]
    for i, heightmap in enumerate(data):
        for j, height in enumerate(heightmap):
            if height != '9':
                basinSize = measureBasin(data, i, j, 0, [])
                if basinSize > min(largestBasinSizes):
                    largestBasinSizes[largestBasinSizes.index(min(largestBasinSizes))] = basinSize
    return largestBasinSizes[0] * largestBasinSizes[1] * largestBasinSizes[2]

with open('data.txt') as f:
    data = f.readlines()
    data = [line.replace('\n', '') for line in data]

lowPointRisksSum = sumLowPointRisks(data.copy())
basinSizes = multiplyThreeLargestBasins(data.copy())

print(lowPointRisksSum)
print(basinSizes)
