import numpy as np

def oldPolicy(data):
    valid = 0
    for element in data:
        minChars, maxChars = list(map(int, element[0].split("-")))
        count = element[2].count(element[1].replace(":", ""))
        valid += 1 if minChars <= count <= maxChars else 0
    return valid

def newPolicy(data):
    valid = 0
    for element in data:
        first, second = list(map(int, element[0].split("-")))
        target = element[1].replace(":", "")
        valid += 1 if (element[2][first - 1] == target) ^ (element[2][second - 1] == target) else 0
    return valid

data = np.genfromtxt('data.txt', delimiter = " ", dtype = "str")

old = oldPolicy(data)
new = newPolicy(data)