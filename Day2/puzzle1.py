score = 0
file = open('Day2\input.txt', 'r')
count = 0

inputArray = []

while True:
    count += 1

    line = file.readline()

    if not line:
        break

    inputArray.append(line)

for x in range(len(inputArray)):
    
    oppChoice = inputArray[x][0:1]
    myChoice = inputArray[x][2:3]
    
    if (oppChoice == 'A' and myChoice == 'X'):
        score = score + 4
    elif (oppChoice == 'B' and myChoice == 'X'):
        score = score + 1
    elif (oppChoice == 'C' and myChoice == 'X'):
        score = score + 7
    elif (oppChoice == 'A' and myChoice == 'Y'):
        score = score + 8
    elif (oppChoice == 'B' and myChoice == 'Y'):
        score = score + 5
    elif (oppChoice == 'C' and myChoice == 'Y'):
        score = score + 2
    elif (oppChoice == 'A' and myChoice == 'Z'):
        score = score + 3
    elif (oppChoice == 'B' and myChoice == 'Z'):
        score = score + 9
    elif (oppChoice == 'C' and myChoice == 'Z'):
        score = score + 6


print(score)