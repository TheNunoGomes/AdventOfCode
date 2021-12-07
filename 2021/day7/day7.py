
def distanceConsumptionConstant(data, target):
    return sum([abs(position-target) for position in data])
    
def distanceConsumptionArithmetic(data, target):    
    return sum([sum([i for i in range(1, abs(position-target)+1)]) for position in data])
    

def alignCrabsConstant(data):
    return min([distanceConsumptionConstant(data, target) for target in range(0, max(data))])

def alignCrabsArithmetic(data):
    return min([distanceConsumptionArithmetic(data, target) for target in range(0, max(data))])


with open('data.txt') as f:
    data = f.readlines()
    data = [int(crab) for crab in data[0].split(',')]
 
print(alignCrabsConstant(data))
print(alignCrabsArithmetic(data))


