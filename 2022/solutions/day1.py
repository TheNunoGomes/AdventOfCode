import numpy as np

def splitElfCalories(data):
    return [[int(calories) for calories in elf] for elf in [calories.split(' ') for calories in ' '.join(data).split('  ')]]

def countCaloriesByElf(data):
    return [sum(elfCalories) for elfCalories in splitElfCalories(data)]


def part1(data):
    maxCalories = 0
    currentCalories = 0
    for calories in data:
        maxCalories = max(currentCalories, maxCalories)
        currentCalories = currentCalories + int(calories) if calories.isdigit() else 0

    return maxCalories

def part2(data):
    caloriesByElf = countCaloriesByElf(data)
    maxCalories = 0

    for i in range(0, 3):
        currentMaxCalories = max(caloriesByElf)
        maxCalories += currentMaxCalories
        caloriesByElf.pop(caloriesByElf.index(currentMaxCalories))
    
    return maxCalories