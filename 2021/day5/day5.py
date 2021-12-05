def getSlope(a, b):
    return 1 if a < b else -1

def ortogonalVents(segments):
    vents = {}
    for segment in segments:
        if segment['x1'] == segment['x2']:
            x = segment['x1']
            lower, upper = sorted([segment['y1'], segment['y2']])
            for y in range(lower, upper+1):
                if not f"{x},{y}" in vents:
                    vents[f"{x},{y}"] = 1
                else:
                    vents[f"{x},{y}"] += 1
        elif segment['y1'] == segment['y2']:
            y = segment['y1']
            lower, upper = sorted([segment['x1'], segment['x2']])
            for x in range(lower, upper+1):
                if not f"{x},{y}" in vents:
                    vents[f"{x},{y}"] = 1
                else:
                    vents[f"{x},{y}"] += 1
        
    return len([vents[key] for key in vents if vents[key] > 1])

def diagonalVents(segments):
    vents = {}
    for segment in segments:
        if segment['x1'] == segment['x2']:
            x = segment['x1']
            lower, upper = sorted([segment['y1'], segment['y2']])
            for y in range(lower, upper+1):
                if not f"{x},{y}" in vents:
                    vents[f"{x},{y}"] = 1
                else:
                    vents[f"{x},{y}"] += 1
        elif segment['y1'] == segment['y2']:
            y = segment['y1']
            lower, upper = sorted([segment['x1'], segment['x2']])
            for x in range(lower, upper+1):
                if not f"{x},{y}" in vents:
                    vents[f"{x},{y}"] = 1
                else:
                    vents[f"{x},{y}"] += 1
        else:
            x_slope = getSlope(segment['x1'], segment['x2'])
            y_slope = getSlope(segment['y1'], segment['y2'])
            
            lower, upper = sorted([segment['y1'], segment['y2']])
            
            x = segment['x1']
            y = segment['y1']
            
            for _ in range(lower, upper+1):
                if not f"{x},{y}" in vents:
                    vents[f"{x},{y}"] = 1
                else:
                    vents[f"{x},{y}"] += 1
                x += x_slope
                y += y_slope
        
    return len([vents[key] for key in vents if vents[key] > 1])

with open('data.txt') as f:
    data = [line.replace('\n', '').split(' -> ') for line in f.readlines()]

segments = []

for segment in data:
    segments.append(
        {
            'x1': int(segment[0].split(',')[0]),
            'y1': int(segment[0].split(',')[1]),
            'x2': int(segment[1].split(',')[0]),
            'y2': int(segment[1].split(',')[1]),
        })

ortogonalVents = ortogonalVents(segments)
diagonalVents = diagonalVents(segments)

print(ortogonalVents, diagonalVents)
