import numpy as np

def calculateCollisions(data, slope, startPos):
    collisions = 0
    pos = startPos
    for i, line in enumerate(data):
        if i % slope[1] != 0:
            continue
        else:
            collisions += 1 if line[pos] == "#" else 0
        
        pos += slope[0]
        pos -= len(line) if pos >= len(line) else 0
        
    return collisions
    
with open("data.txt") as f:
    data = [element.replace(f"\n", "") for element in  f.readlines()]

slopes = np.array([[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]])
startPos = 0
collisions = 1

for slope in slopes:
    collisions *= calculateCollisions(data, slope, startPos)