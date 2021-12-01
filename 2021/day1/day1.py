import numpy as np

def depthIncreases(data):
    return len([depth for i, depth in enumerate(data) if i > 0 and data[i] > data[i-1]])

  
def slidingWindow(data):
    return len([depth for i, depth in enumerate(data) if i > 2 and data[i] > data[i-3]])

data = np.genfromtxt('data.txt', dtype="int")

increases = depthIncreases(data)
slidingWindow = slidingWindow(data)

print(increases)
print(slidingWindow)