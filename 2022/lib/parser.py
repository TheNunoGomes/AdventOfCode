from datetime import datetime

today = datetime.now()
dayFlags = ["-d", "--day"]
partFlags = ["-p", "--part"]
testFlags = ['-t', '--test']
recognizedFlags = dayFlags + partFlags + testFlags

def isPuzzleReleased(presentDatetime, puzzleDay):
    return presentDatetime.year > 2022 or presentDatetime.day >= puzzleDay

def argParser(args):
    unreleasedPuzzle = False
    invalidDay = False
    invalidPart = False
    useTestDataset = False
    unrecognizedArguments = []
    missingArguments = []
    currentFlag = ''
    
    for i, arg in enumerate(args):
        if arg in dayFlags:
            if i == len(args)-1:
                missingArguments.append('/'.join(dayFlags))
                continue
            
            currentFlag = arg
            
            if args[i+1].isdigit():
                day = int(args[i+1])
                if day > 0 and day < 26:
                    unreleasedPuzzle = not isPuzzleReleased(today, day)
                else:
                    invalidDay = True
                continue
            
            if(args[i+1] in recognizedFlags):
                missingArguments.append('/'.join(dayFlags))
                continue
            
            unrecognizedArguments.append(args[i+1])
            continue

        if arg in partFlags:
            if i == len(args)-1:
                missingArguments.append('/'.join(partFlags))
                continue
            
            currentFlag = arg

            if args[i+1].isdigit():
                part = int(args[i+1])
                invalidPart = part not in [1, 2]
                continue

            if args[i+1] in recognizedFlags:
                missingArguments.append('/'.join(partFlags))
                continue

            unrecognizedArguments.append(args[i+1])
            continue
        
        if arg in testFlags:
            useTestDataset = True
            continue
        
        if currentFlag:
            currentFlag = ''
            continue
        
        unrecognizedArguments.append(arg)
            
    if len(unrecognizedArguments):
        raise Exception(f"Unrecognized arguments: {' '.join(unrecognizedArguments)}")
    if len(missingArguments):
        raise Exception(f"Missing argument for {'/'.join(missingArguments)}")
    if not ('day' in locals()):
        raise Exception('Missing argument for -d/--day')
    if not ('part' in locals()):
        raise Exception('Missing argument for -p/--part')
    if unreleasedPuzzle:
        raise Exception("This day's puzzle has not been released yet!")
    if invalidDay:
        raise Exception('Invalid day selected.')
    if invalidPart:
        raise Exception('Puzzle part must be 1 or 2.')

    return day, part, useTestDataset
