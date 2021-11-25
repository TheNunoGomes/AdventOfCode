import numpy as np

def getEdgeSeats(data):
    minSeat = 1023
    maxSeat = 0
    for seat in data:
        seatId = getSeatId(seat)
        minSeat = seatId if seatId < minSeat else minSeat
        maxSeat = seatId if seatId > maxSeat else maxSeat
    return minSeat, maxSeat

def getSeatId(seat):
    rowBinary = seat[0:7].replace('F', '0').replace('B', '1')
    colBinary = seat[7:10].replace('L', '0').replace('R', '1')
    return int(rowBinary, 2) * 8 + int(colBinary, 2)


def mySeat(data):
    missingSeats = []
    minSeat, maxSeat = getEdgeSeats(data)
    for seatId in np.arange(minSeat, maxSeat):
        code = str(bin(seatId)).replace('0b', '').zfill(10)
        code = f"{code[0:7].replace('0', 'F').replace('1', 'B')}{code[7:10].replace('0', 'L').replace('1', 'R')}"
        if code not in data:
            missingSeats.append(code)
            
    return missingSeats

data = np.genfromtxt('data.txt', dtype = "str")

_, highest = getEdgeSeats(data)
mySeat = getSeatId(mySeat(data)[0])

print(highest)
print(mySeat)