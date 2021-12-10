CORRUPTION_SCORE = {
        '>': 25137,
       '}': 1197,
        ']': 57,
        ')': 3
    }

INCOMPLETE_SCORE = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

def matchingCharacters(opener, closer):
    return closer == [')', ']', '}', '>'][['(', '[', '{', '<'].index(opener)]

def isOpener(char):
    return char in ['(', '[', '{', '<']

def isCloser(char):
    return char in [')', ']', '}', '>']

def hasSyntaxError(chunk, i):
    closerIndex = i
    while closerIndex < len(chunk)-1 and isOpener(chunk[closerIndex]):
        closerIndex += 1
    
    if isOpener(chunk[closerIndex]):
        return 0, chunk
    elif closerIndex >= len(chunk) - 1:
        return 0, chunk[:-2]

    if matchingCharacters(chunk[closerIndex-1], chunk[closerIndex]):       
        return hasSyntaxError(chunk[:closerIndex-1] + chunk[closerIndex+1:], closerIndex-1)

    return CORRUPTION_SCORE[chunk[closerIndex]], ''

def middleScore(chunk):
    chunkScore = 0
    for char in reversed(chunk):
        chunkScore *= 5
        chunkScore += INCOMPLETE_SCORE[char]
    return chunkScore

def syntaxScore(data):
    total = 0
    incomplete = []
    middle = []
    for line in data:
        score, chunk = hasSyntaxError(line, 0)
        total += score
        incomplete.append(chunk)
    middle = sorted([middleScore(chunk) for chunk in incomplete if chunk != ''])
    middle = middle[int((len(middle) - 1) / 2)]
    return total, middle

with open('data.txt') as f:
    data = f.readlines()
    data = [line.replace('\n', '') for line in data]
    
score, middle = syntaxScore(data.copy())
print(score, middle)