def numberByLength(encodedNumber):
    if len(encodedNumber) == 2:
        return 1
    elif len(encodedNumber) == 4:
        return 4
    elif len(encodedNumber) == 3:
        return 7
    elif len(encodedNumber) == 7:
        return 8
    else:
        return False
    
def decodeByLength(data):
    codes = [False for n in range(10)]
    for encodedNumber in data:
        decoded = numberByLength(encodedNumber)
        if decoded and not codes[decoded]:
            codes[decoded] = sort(encodedNumber)
            if len([code for code in codes if code]) == 4:
                break
    return codes

def missingChars(source, target):
    return [char for char in sorted(source) if char not in sorted(target)]

def sort(string):
    return "".join(sorted(string))

def decodeThree(sequence, code1, code5):    
    for encodedNumber in sequence:
        if len(encodedNumber) == 5 and sort(encodedNumber) != code5:
            missingCharacters = missingChars(code1, encodedNumber)
            if len(missingCharacters) == 0:
                return sort(encodedNumber)
    return False

def decodeTwo(sequence, codes):
    for encodedNumber in sequence:
        if sort(encodedNumber) not in codes:
            return sort(encodedNumber)
    return False

def decodeFive(sequence, code8, code6):
    for encodedNumber in sequence:
        if len(encodedNumber) == 5:
            missing6Char = missingChars(code8, code6)[0]
            missingCharacters = missingChars(code8, encodedNumber)
            if missing6Char in missingCharacters:
                return sort(encodedNumber)
    return False

def decodeSix(sequence, code8, code1):
    for encodedNumber in sequence:
        if len(encodedNumber) == 6:
            char = missingChars(code8, encodedNumber)[0]
            if char in sorted(code1):
                return sort(encodedNumber)
    return False

def decodeNine(sequence, code8, code6, code5):
    for encodedNumber in sequence:
        if len(encodedNumber) == 6 and sort(encodedNumber) != code6:
            missingChar = missingChars(code8, encodedNumber)[0]
            missing5Chars = missingChars(code8, code5)
            if missingChar in missing5Chars:
                return sort(encodedNumber)
    return False 

def decodeZero(sequence, codes):
    for encodedNumber in sequence:
        if len(encodedNumber) == 6 and sort(encodedNumber) not in codes:
            return sort(encodedNumber)
    return False 

def decode(sequence):
    codes = decodeByLength(sequence) # Decode 1, 4, 7 and 8
    codes[6] = decodeSix(sequence, codes[8], codes[1])
    codes[5] = decodeFive(sequence, codes[8], codes[6])
    codes[9] = decodeNine(sequence, codes[8], codes[6], codes[5])
    codes[0] = decodeZero(sequence, codes)
    codes[3] = decodeThree(sequence, codes[1], codes[5])
    codes[2] = decodeTwo(sequence, codes)
    return codes

def count1478s(data):
    return sum([len([number for number in output if len(number) in [2, 4, 3, 7]]) for output in data])

def sumOutputs(data):
    total = 0
    for line in data:
        codes = decode(line[0].split(' '))
        output = line[1].split(' ')
        
        total += int("".join([str(codes.index(sort(digit))) for digit in output]))
    return total

with open('data.txt') as f:
    data = f.readlines()
    data = [display.replace('\n', '').split(' | ') for display in data]
    
outputs = [line[1].split(' ') for line in data]

count = count1478s(outputs)
sumOfOutputs = sumOutputs(data)

print(sumOfOutputs)