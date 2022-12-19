from lib.math import getManhatanDistance

class Sensor:
    def __init__(self, position, closestBeacon):
        self.position = position
        self.closestBeacon = closestBeacon
        self.distanceToBeacon = getManhatanDistance(position, closestBeacon)

    def __str__(self):
        return f"Sensor in position {self.position}. Closest beacon in position {self.closestBeacon} at a distance of {self.distanceToBeacon}"

    def canDetectLine(self, lineNumber):
        sensorY = self.position[1]
        distanceToLine = abs(sensorY - lineNumber)
        if distanceToLine > self.distanceToBeacon:
            return False

        return abs(distanceToLine - self.distanceToBeacon)

def parseSensor(line):
    words = line.split(' ')
    sensorX = int(words[2].split('=')[1][:-1])
    sensorY = int(words[3].split('=')[1][:-1])
    beaconX = int(words[8].split('=')[1][:-1])
    beaconY = int(words[9].split('=')[1])
    return Sensor((sensorX, sensorY), (beaconX, beaconY))

def rangesCanBeSimplified(ranges):
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if getUniqueRange(ranges[i], ranges[j]):
                return True
    return False

def rangeIsContained(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    start1ContainedInRange2 = start1 >= start2 and start1 <= end2
    start2ContainedInRange1 = start2 >= start1 and start2 <= end1
    end1ContainedInRange2 = end1 >= start2 and end1 <= end2
    end2ContainedInRange1 = end2 >= start1 and end2 <= end1
    return start1ContainedInRange2 or start2ContainedInRange1 or end1ContainedInRange2 or end2ContainedInRange1

def getUniqueRange(range1, range2):
    start1, end1 = range1
    start2, end2 = range2
    if rangeIsContained(range1, range2):
        return [min(start1, start2), max(end1, end2)]
    return False

def getUniqueRangesWithoutBeacons(rangesWithoutBeacons):
    simplifiedRanges = rangesWithoutBeacons
    while rangesCanBeSimplified(simplifiedRanges):
        uniqueRanges = []
        # print('Unsimplified', simplifiedRanges)
        for i in range(len(simplifiedRanges) - 1):
            range1 = simplifiedRanges[i]
            for j in range(i + 1, len(simplifiedRanges)):
                range2 = simplifiedRanges[j]
                uniqueRange = getUniqueRange(range1, range2)
                # print('Comparing', range1, range2)
                # print('Unique range', uniqueRange)
                # input('\n')
                if not uniqueRange:
                    continue
                range1 = uniqueRange
            # print('Range 1', range1)
            uniqueRanges.append(range1)
            # print(uniqueRanges)
            # input('\n')
        simplifiedRanges = uniqueRanges
    return simplifiedRanges

def countPositions(ranges):
    if rangesCanBeSimplified(ranges):
        raise Exception('This is not fully simplified')
    return sum([uniqueRange[1] - uniqueRange[0] for uniqueRange in ranges])

def part1(data):
    lineNumber = 2000000
    rangesWithoutBeacons = []
    for line in data:
        sensor = parseSensor(line)
        sensorX = sensor.position[0]
        distanceDifference = sensor.canDetectLine(lineNumber)
        if distanceDifference == False:
            continue
        
        rangesWithoutBeacons.append([sensorX - distanceDifference, sensorX + distanceDifference])
    uniqueRanges = getUniqueRangesWithoutBeacons(rangesWithoutBeacons)
    print(uniqueRanges)
    return countPositions(uniqueRanges)

def part2(data):
    return 1