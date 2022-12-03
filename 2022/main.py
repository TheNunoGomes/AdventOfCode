import sys
from lib.parser import argParser

day, part, test = argParser(sys.argv[1:])

exec(f"from solutions.day{day} import part{part} as solve")

with open(f"datasets/day{day}_{'test' if test else 'challenge'}.txt") as f:
    data = f.readlines()
    data = [line.replace('\n', '') for line in data]

print(f"Day {day} | Part {part} | {'Test' if test else 'Challenge'} dataset")
print(solve(data))

