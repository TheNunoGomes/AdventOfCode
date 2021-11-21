import numpy as np

def calculateCollisions(data, slope, startPos):
    collisions = 0
    pos = startPos
    for i, line in enumerate(data):
        
        return
    
with open("data.txt") as f:
    data = [element.replace(f"\n", "") for element in  f.readlines()]

slope = np.array([3, 1])
startPos = 0

collisions = calculateCollisions(data, slope, startPos)

print(collisions)