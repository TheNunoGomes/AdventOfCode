def findMarker(signal, markerLength):
    currentIndex = 0
    while True:
        potentialMarker = signal[currentIndex:currentIndex + markerLength]
        duplicates = [char for char in potentialMarker if potentialMarker.count(char) > 1]
        if not len(duplicates):
            return currentIndex + markerLength

        currentIndex += potentialMarker.index(duplicates[0]) + 1            
    
def part1(data):
    return findMarker(data[0], 4) if len(data) == 1 else [findMarker(signal, 4) for signal in data]


def part2(data):
    return findMarker(data[0], 14) if len(data) == 1 else [findMarker(signal, 14) for signal in data]