def calculateRoundScorePart1(player, opponent):
    if player == opponent:
        score = player + 3
    elif (player == 1 and opponent == 2) or (player == 2 and opponent == 3) or (player == 3 and opponent == 1):
        score = player
    else:
        score = player + 6
    return score

def calculateRoundScorePart2(player, opponent):
    if opponent == 'A' and player == 'X':
        return 3
    if opponent == 'A' and player == 'Y':
        return 4
    if opponent == 'A' and player == 'Z':
        return 8

    if opponent == 'B' and player == 'X':
        return 1
    if opponent == 'B' and player == 'Y':
        return 5
    if opponent == 'B' and player == 'Z':
        return 9

    if opponent == 'C' and player == 'X':
        return 2
    if opponent == 'C' and player == 'Y':
        return 6
    if opponent == 'C' and player == 'Z':
        return 7


def part1(data):
    totalScore = 0
    for play in data:
        opponent, player = play.split(' ')
        player = 1 if player == 'X' else 2 if player == 'Y' else 3
        opponent = 1 if opponent == 'A' else 2 if opponent == 'B' else 3
        
        totalScore += calculateRoundScorePart1(player, opponent)
    return totalScore

def part2(data):
    totalScore = 0
    for play in data:
        opponent, player = play.split(' ')
        
        totalScore += calculateRoundScorePart2(player, opponent)
    return totalScore