import sys

class Cave:
    def __init__(self, data):
        self.generateAir(data)
        self.generateSource()
        self.generateRocks(data)

    def __str__(self):
        string = ''
        for row in self.positions:
            for position in row:
                string += position.__str__()
            string += '\n'
        return string

    def generateSource(self):
        x, y = 500 - self.minX, 0
        self.positions[y][x] = '+'
        self.source = (x, y)

    def getCorners(self, data):
        minX = sys.maxsize
        maxX = 0
        maxY = 0
        for line in data:
            for coordinate in line.split(' -> '):
                x, y = [int(c) for c in coordinate.split(',')]
                minX = min(minX, x)
                maxX = max(maxX, x)
                maxY = max(maxY, y)
        return (minX, 0), (maxX, maxY)

    def generateAir(self, data):
        topLeft, bottomRight = self.getCorners(data)
        maxX, maxY = bottomRight
        self.minX, _ = topLeft

        self.positions = []
        for y in range(maxY + 1):
            self.positions.append([])
            for x in range(maxX - self.minX + 1):
                self.positions[y].append('.')
                
    
    def generateRocks(self, data):
        for line in data:
            rockLineEdges = line.split(' -> ')
            for i in range(len(rockLineEdges) - 1):
                self.generateRocksInLine(rockLineEdges[i].split(','), rockLineEdges[i+1].split(','))
        return []
        
    def generateRocksInLine(self, start, end):
        startX, startY = int(start[0]), int(start[1])
        endX, endY = int(end[0]), int(end[1])
        if startX != endX:
            incrementFactor = 1 if endX > startX else -1
            for rockIndex in range(abs(endX - startX) + 1):
                rockX = startX + (incrementFactor * rockIndex)
                positionX = rockX - self.minX
                positionY = rockY = startY
                self.positions[positionY][positionX] = '#'
        elif startY != endY:
            incrementFactor = 1 if endY > startY else -1
            for rockIndex in range(abs(endY - startY) + 1):
                positionY = startY + (incrementFactor * rockIndex)
                positionX = startX - self.minX
                self.positions[positionY][positionX] = '#'

    def generateSand(self, infiniteFloor = False):
        numberOfSandGrains = 0
        while True:
            sandX, sandY = self.source[0], self.source[1]
            while True:
                if self.positions[self.source[1]][self.source[0]] == 'o':
                    return numberOfSandGrains
                self.positions[sandY][sandX] = 'o'
                
                if infiniteFloor:
                    if sandX - 1 < 0:
                        self.expandLeft()
                        sandX += 1
                    elif sandX + 1 > len(self.positions[0]) - 1:
                        self.expandRight()
                elif sandY + 1 == len(self.positions):
                        return numberOfSandGrains


                if self.positions[sandY+1][sandX] == '.':
                    # print('Going down')
                    self.positions[sandY][sandX] = '.'
                    sandY += 1
                    continue
                if self.positions[sandY+1][sandX-1] == '.':
                    self.positions[sandY][sandX] = '.'
                    sandY += 1
                    sandX -= 1   
                    continue    
                if self.positions[sandY+1][sandX+1] == '.':
                    self.positions[sandY][sandX] = '.'
                    sandY += 1
                    sandX += 1
                    continue
                numberOfSandGrains += 1
                break

    def generateInfiniteFloor(self, height):
        for _ in range(height):
            self.positions.append([])
            for _ in range(len(self.positions[0])):
                self.positions[-1].append('.')

        for i in range(len(self.positions[0])):
                self.positions[-1][i] = '#'
        
        return self
    
    def expandLeft(self):
        for y in range(len(self.positions) - 1):
            self.positions[y].insert(0, '.')
        self.positions[-1].insert(0, '#')
        self.source = (self.source[0] + 1, self.source[1])

    def expandRight(self):
        for y in range(len(self.positions) - 1):
            self.positions[y].insert(len(self.positions[0]) - 1, '.')
        self.positions[-1].insert(len(self.positions[0]) - 1, '#')

def part1(data):
    cave = Cave(data)
    return cave.generateSand()

def part2(data):
    cave = Cave(data)
    return cave.generateInfiniteFloor(2).generateSand(True)