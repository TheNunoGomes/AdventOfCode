def fishAfterDays(data, day):
    fishes = [0 for n in range(9)]
    for fishDays in data:
        fishes[fishDays] += 1
    for day in range(day):
        children = fishes[0]
        
        for i in range(8):
            fishes[i] = fishes[i+1]
        
        fishes[6] += children
        fishes[8] = children
        
    return sum(fishes)


with open('data.txt') as f:
    data = f.readlines()
    data = [int(fish) for fish in data[0].split(',')]
    
after80Days = fishAfterDays(data.copy(), 80)
after256Days = fishAfterDays(data.copy(), 256)
print(after80Days)
print(after256Days)