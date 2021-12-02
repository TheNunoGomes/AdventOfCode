import numpy as np

def calculateDepth(data):
    return sum([instruction[1] for instruction in data if instruction[0] == "forward"]), sum([instruction[1] for instruction in data if instruction[0] == "down"]) - sum([instruction[1] for instruction in data if instruction[0] == "up"])


def calculateDepthWithAim(data):
    depth, aim = 0, 0
    for instruction in data:
        direction, value = instruction
        if direction == "forward":
            depth += value*aim
        elif direction == "up":
            aim -= value
        elif direction == "down":
            aim += value
            
    return sum([instruction[1] for instruction in data if instruction[0] == "forward"]), depth

data = np.genfromtxt('data.txt', dtype = None, encoding = None)

distance1, depth1 = calculateDepth(data)
distance2, depth2 = calculateDepthWithAim(data)

print(distance1*depth1)
print(distance2*depth2)