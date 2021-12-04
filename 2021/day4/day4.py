class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.complete = False
    
    def checkRows(self, number):
        for row in self.rows:
            row.checkNumber(number)
            if row.isComplete():
                return True
        return False
                
    def checkCols(self, number):
        for col in self.cols:
            col.checkNumber(number) 
            if col.isComplete():
                return True
        return False
    
    def isComplete(self):
        for row in self.rows:
            if row.isComplete():
                return True
        for col in self.cols:
            if col.isComplete():
                return True
        return False
    
    def printWinningSequence(self):
        for row in self.rows:
            if row.complete:
                print(row.numbers)
                return
        for col in self.cols:
            if col.complete:
                print(col.numbers)
                return
    
    def printBoard(self):
        for row in self.rows:
            print(row.numbers)
            
            
    def printBoardTransposed(self):
        for col in self.cols:
            print(col.numbers)
            
    def sumUncheckedNumbers(self):
        boardSum = 0
        for row in self.rows:
            boardSum += row.sumUncheckedNumbers()
        return boardSum
    
class Row:
    def __init__(self, numbers):
        self.numbers = numbers
        self.checkedNumbers = []
        self.complete = False
        
    def checkNumber(self, number):
        if number in self.numbers and number not in self.checkedNumbers:
            self.checkedNumbers.append(number)
            return True
        return False
    
    def isComplete(self):
        if sorted(self.checkedNumbers) == sorted(self.numbers):
            self.complete = True
            return True
        else:
            return False
        
    def sumUncheckedNumbers(self):
        rowSum = 0
        for number in self.numbers:
            rowSum += number if number not in self.checkedNumbers else 0
        return rowSum
    
class Column:
    def __init__(self, numbers):
        self.numbers = numbers
        self.checkedNumbers = []
        self.complete = False
        
    def checkNumber(self, number):
        if number in self.numbers and number not in self.checkedNumbers:
            self.checkedNumbers.append(number)
            return True
        return False
    
    def isComplete(self):
        if sorted(self.checkedNumbers) == sorted(self.numbers):
            self.complete = True
            return True
        else:
            return False
    
    def addNumber(self, number):
        self.numbers.append(number)
        
def playBingo(numberSeq, boards):
    boardsCopy = list(boards)
    for number in numberSeq:
        for board in boardsCopy:
            board.checkRows(number)
            board.checkCols(number)
            if board.isComplete():
                return board.sumUncheckedNumbers() * number
            
def loseBingo(numberSeq, boards):
    boardsCopy = list(boards)
    completeBoards = 0
    for number in numberSeq:
        for board in boardsCopy:
            if board.isComplete():
                continue
            board.checkRows(number)
            board.checkCols(number)
            if board.isComplete():
                completeBoards += 1
            if len(boardsCopy) == completeBoards:
                return board.sumUncheckedNumbers() * number


def read_blocks(file):
    block = ''
    for line in file:
        if line.startswith('>') and len(block)>0:
            yield block
            block = ''
        block += line
    yield block
    
def parseFile(fileName):
    with open(fileName) as f:
        for block in read_blocks(f):
            data = block.split('\n\n')
            numberSeq = [int(number) for number in data[0].split(',')]
            data = data[1:]
            boards = []
            for i, element in enumerate(data):
                board = element.split('\n')
                boardRows = []
                boardCols = []
                
                for j, line in enumerate(board):
                    lsplit = [int(n) for n in line.split(' ') if n != '']
                    for n, _ in enumerate(lsplit): 
                        if n > len(boardCols) - 1:
                            boardCols.append(Column([]))
                        boardCols[n].addNumber(lsplit[n])
                    boardRows.append(Row(lsplit))
                    
                boards.append(Board(boardRows, boardCols))
    return numberSeq, boards
    
boards1 = []
boards2 = []

numberSeq, boards1 = parseFile('data.txt')
_, boards2 = parseFile('data.txt')
 
print(playBingo(numberSeq, boards1))
print(loseBingo(numberSeq, boards2))
