import numpy as np

def computeExpensesOf2(data, target):
    its = 0
    for i in range(len(data)):
        if data[i] >= target:
            its += 1
            continue
        for j in range(i+1, len(data)):
            its += 1
            if data[i] + data[j] == target:
                return [data[i] * data[j], its]
                        
def computeExpensesOf3(data, target):
    its = 0
    for i in range(len(data)):
        if data[i] >= 2020:
            its += 1
            continue
        for j in range(i+1, len(data)):
            if data[i] + data[j] >= target:
                its += 1
                continue
            for k in range(j+1, len(data)):
                its += 1
                if data[i] + data[j] + data[k] == target:
                    return [data[i] * data[j] * data[k], its]

data = np.genfromtxt('data.txt', dtype="int")

target = 2020
expensesOf2, its2 = computeExpensesOf2(data, target)
expensesOf3, its3 = computeExpensesOf3(data, target)
