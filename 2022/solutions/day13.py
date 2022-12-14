import ast

def stringToList(stringList):
    return ast.literal_eval(stringList)

def compareInputs(left, right, inputIsSubArray = False):
    i = 0
    while len(right):
        if not len(left):
            return True

        leftValue = left.pop(0)
        rightValue = right.pop(0)

        if type(leftValue) == list and type(rightValue) == list:
            inputComparison = compareInputs(list(leftValue), list(rightValue), True)
            if inputComparison != None:
                return inputComparison
            continue
        elif type(leftValue) == list:
            inputComparison = compareInputs(list(leftValue), list([rightValue]), True)
            if inputComparison != None:
                return inputComparison
            continue
        elif type(rightValue) == list:
            inputComparison = compareInputs(list([leftValue]), list(rightValue), True)
            if inputComparison!= None:
                return inputComparison
            continue

        if leftValue > rightValue:
            return False
        if leftValue < rightValue:
            return True

    if len(left):
        return False
    
    if inputIsSubArray:
        return None

    return True

def sortInputs(inputs):
    sortedInputs = []
    for newInput in inputs:
        newInputIndex = 0
        appendInput = True
        for i in sortedInputs:
            orderCorrect = compareInputs(list(newInput), list(i))
            if orderCorrect:
                sortedInputs.insert(newInputIndex, newInput)
                appendInput = False
                break
            newInputIndex += 1
        if appendInput:
            sortedInputs.append(newInput)
    return sortedInputs

def findDividerPackets(inputs):
    divider1, divider2 = len(inputs), len(inputs)
    for i, sortedInput in enumerate(inputs, 1):
        if compareInputs(list([[2]]), list(sortedInput)):
            divider1 = i
            break
    for i, sortedInput in enumerate(inputs[divider1:], 1):
        if compareInputs(list([[6]]), list(sortedInput)):
            divider2 = divider1 + i
            break
    return divider1, divider2

def getDecoderKey(dividers):
    return dividers[0] * dividers[1]

def part1(data):
    return sum([int((i/3)+1) for i in range(0, len(data), 3) if compareInputs(list(stringToList(data[i])), list(stringToList(data[i+1])))])

def part2(data):
    inputs = [stringToList(i) for i in data if i != '']
    inputs.append([[2]])
    inputs.append([[6]])
    
    return getDecoderKey(findDividerPackets(sortInputs(inputs)))