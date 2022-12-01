import sys
from lib.parser import argParser

day, part, test = argParser(sys.argv[1:])
print(day, part, test)

exec(f"from days.day{day} import part{part} as solve")

with open(f"data/day{day}_{'test' if test else 'challenge'}.txt") as f:
    data = f.readlines()
    data = [line.replace('\n', '') for line in data]

print(solve(data))

