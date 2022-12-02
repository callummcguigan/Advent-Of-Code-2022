score = 0

count = 0

inputArray = []

with open('Day2\input.txt') as f:
    inputArray = f.readlines()

for x in range(len(inputArray)):
    
    oppChoice = inputArray[x][0:1]
    outcome = inputArray[x][2:3]
    
    A = 1
    B = 2
    C = 3

    X = 0
    Y = 3
    Z = 6

    if (outcome == 'X'):
        if (oppChoice == 'A'):
            score += (X + C)
        elif (oppChoice == 'B'):
            score += (X + A)
        elif (oppChoice == 'C'):
            score += (X + B)
    if (outcome == 'Y'):
        if (oppChoice == 'A'):
            score += (Y + A)
        elif (oppChoice == 'B'):
            score += (Y + B)
        elif (oppChoice == 'C'):
            score += (Y + C)
    if (outcome == 'Z'):
        if (oppChoice == 'A'):
            score += (Z + B)
        elif (oppChoice == 'B'):
            score += (Z + C)
        elif (oppChoice == 'C'):
            score += (Z + A)
        
print(score)