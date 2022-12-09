class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.nextKnot = None

    def __str__(self):
        # currentKnot = "oo"
        currentKnot = f"({self.x}, {self.y})"
        if self.nextKnot:
            currentKnot += f"-{self.nextKnot}"
        return currentKnot

    def addKnot(self):
        self.nextKnot = Knot()
        return self.nextKnot

    def move(self, vector):
        ix, iy = self.x, self.y
        vx, vy = vector
        self.x += vx
        self.y += vy

        if not self.nextKnot:
            return

        dx, dy = self.x - self.nextKnot.x, self.y - self.nextKnot.y
        v = (0, 0)

        if dx == 2 and dy == 0:
            v = (1, 0)
        elif (dx == 2 and dy == 1) or (dx == 2 and dy == 2):
            v = (1, 1)
        elif (dx == 2 and dy == -1) or (dx == 2 and dy == -2):
            v = (1, -1)

        elif dx == -2 and dy == 0:
            v = (-1, 0)
        elif (dx == -2 and dy == 1) or (dx == -2 and dy == 2):
            v = (-1, 1)
        elif (dx == -2 and dy == -1) or (dx == -2 and dy == -2):
            v = (-1, -1)

        elif dy == 2 and dx == 0:
            v = (0, 1)
        elif (dy == 2 and dx == 1) or (dy == 2 and dx == 2):
            v = (1, 1)
        elif (dy == 2 and dx == -1) or (dy == 2 and dx == -2):
            v = (-1, 1)

        elif dy == -2 and dx == 0:
            v = (0, -1)
        elif (dy == -2 and dx == 1) or (dy == -2 and dx == 2):
            v = (1, -1)
        elif (dy == -2 and dx == -1) or (dy == -2 and dx == -2):
            v = (-1, -1)

        self.nextKnot.move(v)

        
class Rope:
    def __init__(self, size):
        self.startingKnot = Knot()
        currentKnot = self.startingKnot
        for _ in range(size-1):
            currentKnot = currentKnot.addKnot()

    def getTail(self):
        currentKnot = self.startingKnot
        while currentKnot.nextKnot:
            currentKnot = currentKnot.nextKnot
        return currentKnot
        
    def move(self, leadingVector):
        self.startingKnot.move(leadingVector)
        return (self.getTail().x, self.getTail().y)

    def printChain(self):
        return self.startingKnot

def getPositions(data, chainSize):
    rope = Rope(chainSize)
    positions = {}
    for direction, numberOfMoves in [move.split(' ') for move in data]:
        numberOfMoves = int(numberOfMoves)
        if direction == 'R':
            for _ in range(numberOfMoves):
                positions[rope.move((1, 0))] = '#'
        if direction == 'L':
            for _ in range(numberOfMoves):
                positions[rope.move((-1, 0))] = '#'
        if direction == 'U':
            for _ in range(numberOfMoves):
                positions[rope.move((0, 1))] = '#'
        if direction == 'D':
            for _ in range(numberOfMoves):
                positions[rope.move((0, -1))] = '#'
    return len(positions)

def part1(data):
    return getPositions(data, 2)
    

def part2(data):
    return getPositions(data, 10)
    