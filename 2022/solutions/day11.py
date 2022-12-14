class Monkey:
    def __init__(self, monkeyData, number):
        self.number = number
        self.items = [int(item) for item in monkeyData[1][18:].split(', ')]            
        self.operation = monkeyData[2][19:].split(' ')
        self.test = int(monkeyData[3][21:])
        self.trueMonkey = int(monkeyData[4][-1])
        self.falseMonkey = int(monkeyData[5][-1])
        self.itemsInspected = 0

    def sendItemToNextMonkey(self, decreaseWorry, mod = 1):
        arg1 = self.items[0] if self.operation[0] == 'old' else int(self.operation[0])
        arg2 = self.items[0] if self.operation[2] == 'old' else int(self.operation[2])

        self.items = self.items[1:]
        self.itemsInspected += 1

        testWorry = arg1 + arg2 if self.operation[1] == '+' else arg1 * arg2
        if decreaseWorry:
            testWorry = int(testWorry / 3)
            
        testWorry %= mod
        
        if testWorry % self.test == 0:
            return self.trueMonkey, testWorry
        else:
            return self.falseMonkey, testWorry
            
def parseData(data):
    monkeys = []
    for i, line in enumerate(data):
        if line.startswith('Monkey '):
            monkeys.append(Monkey(data[i:i+6], i))

    return monkeys        

def simulateRoundsPart1(monkeys, numberOfRounds):
    for _ in range(numberOfRounds):
        for monkey in monkeys:
            for item in monkey.items:
                nextMonkey, newWorry = monkey.sendItemToNextMonkey(True)
                monkeys[nextMonkey].items.append(newWorry)

    return monkeys
    
def simulateRoundsPart2(monkeys, numberOfRounds):
    mod = 1
    for monkey in monkeys:
        mod *= monkey.test

    for _ in range(numberOfRounds):
        for monkey in monkeys:
            for item in monkey.items:
                nextMonkey, newWorry = monkey.sendItemToNextMonkey(False, mod)
                monkeys[nextMonkey].items.append(newWorry)

    return monkeys


def part1(data):
    monkeys = parseData(data)

    itemsInspected = sorted([m.itemsInspected for m in simulateRoundsPart1(monkeys, 20)])[-2:]
    return itemsInspected[0] * itemsInspected[1]
    

def part2(data):
    monkeys = parseData(data)

    itemsInspected = sorted([m.itemsInspected for m in simulateRoundsPart2(monkeys, 10000)])[-2:]
    return itemsInspected[0] * itemsInspected[1]