def incrementAdjacent(grid, row, col, exceptions):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
        return
    # Top Left
    if row > 0 and col > 0 and [row-1, col-1] not in exceptions:
        grid[row-1][col-1] += 1
    # Top
    if row > 0 and [row-1, col] not in exceptions:
        grid[row-1][col] += 1
    # Top Right
    if row > 0 and col < len(grid[row]) - 1 and [row-1, col+1] not in exceptions:
        grid[row-1][col+1] += 1
    # Left
    if col > 0 and [row, col-1] not in exceptions:
        grid[row][col-1] += 1
    # Right
    if col < len(grid[row]) - 1 and [row, col+1] not in exceptions:
        grid[row][col+1] += 1
    # Bottom Left
    if row < len(grid) - 1 and col > 0 and [row+1, col-1] not in exceptions:
        grid[row+1][col-1] += 1
    # Bottom
    if row < len(grid) - 1 and [row+1, col] not in exceptions:
        grid[row+1][col] += 1
    # Bottom Right
    if row < len(grid) - 1 and col < len(grid[row]) - 1 and [row+1, col+1] not in exceptions:
        grid[row+1][col+1] += 1
    
    return grid

def incrementAll(grid):
    return [[energy+1 for energy in row] for row in grid]

def octopusEnergy(grid):
    flashes = 0
    flashedThisStep = []
    grid = incrementAll(grid.copy())
    while sum([len([energy for energy in energies if energy > 9]) for energies in grid]):
        for row, energies in enumerate(grid):
            for col, energy in enumerate(energies):
                if energy > 9:
                    flashedThisStep.append([row, col])
                    incrementAdjacent(grid.copy(), row, col, flashedThisStep)
                    grid[row][col] = 0
                    flashes += 1
    return flashes, grid

def oneHundredSteps(grid):
    flashes = 0
    grid = data.copy()
    for i in range(100):
        n, grid = octopusEnergy(grid.copy())
        flashes += n
    return flashes

def synchronizedFlashes(grid):
    step = 0
    while True:
        if sum([len([energy for energy in energies if energy == 0]) for energies in grid]) == 100:
            return step
        step += 1
        _, grid = octopusEnergy(grid.copy())

with open('data.txt') as f:
    data = f.readlines()
    data = [[int(c) for c in line.replace('\n', '')] for line in data]
 
flashes = oneHundredSteps(data.copy())
step = synchronizedFlashes(data.copy())

print(flashes)
print(step)