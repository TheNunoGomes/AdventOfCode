import sys

class Map:
    def __init__(self, data):
        self.positions = []
        for y, row in enumerate(data):
            self.positions.append([])
            for x, position in enumerate(row):
                if position == 'S':
                    self.start = Position(x, y, ord('a'))
                    self.positions[y].append(self.start)
                elif position == 'E':
                    self.end = Position(x, y, ord('z'))
                    self.positions[y].append(self.end)
                else:
                    self.positions[y].append(Position(x, y, ord(position)))

        self.start.shortestPath = 0

    def __str__(self):
        string = ''
        for row in self.positions:
            for p in row:
                string += f"{p.shortestPath}\t"
            string += '\n'
        return string

    def getAdjacentPaths(self, currentPosition):
        return [self.positions[adjacentY][adjacentX] for adjacentX, adjacentY in currentPosition.getAdjacentDirections(len(self.positions[0]) - 1, len(self.positions) - 1)]

class Position:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.shortestPath = sys.maxsize

    def getAdjacentDirections(self, maxX, maxY):
        adjacentDirections = []
        if self.x > 0:
            adjacentDirections.append((self.x-1, self.y))
        if self.y > 0:
            adjacentDirections.append((self.x, self.y-1))
        if self.x < maxX:
            adjacentDirections.append((self.x+1, self.y))
        if self.y < maxY:
            adjacentDirections.append((self.x, self.y+1))
        return adjacentDirections
        
    def __str__(self):
        return f"({self.x}, {self.y})"

def findShortestPath(mountainMap):
    positionsToVisit = [mountainMap.start]
    while len(positionsToVisit):
        currentPosition = positionsToVisit.pop(0)
        adjacentPositions = mountainMap.getAdjacentPaths(currentPosition)
        
        for adjacent in adjacentPositions:
            if adjacent.value > currentPosition.value + 1:
                continue
            if adjacent.shortestPath <= currentPosition.shortestPath + 1:
                continue
            
            adjacent.shortestPath = currentPosition.shortestPath + 1
            positionsToVisit.append(adjacent)
    return mountainMap.end.shortestPath


def part1(data):
    mountainMap = Map(data)
    return findShortestPath(mountainMap)

def part2(data):
    mountainMap = Map(data)
    elevationAs = [position for row in mountainMap.positions for position in row if position.value == ord('a')]
    shortestPath = sys.maxsize
    for elevationA in elevationAs:
        mountainMap = Map(data)
        mountainMap.start = elevationA
        mountainMap.start.shortestPath = 0
        shortestPath = min(shortestPath, findShortestPath(mountainMap))
    print(shortestPath)
        