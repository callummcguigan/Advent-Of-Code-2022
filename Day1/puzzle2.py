value = 0
top3 = 0
values = []

file = open('Day1\AOC1.txt', 'r')
count = 0

while True:
    count += 1

    line = file.readline()

    if not line:
        break
    if (line != '\n'):
        value = value + int(line)
    elif (line == '\n'):
        values.append(value)
        value = 0

values.sort(reverse=True)

for x in range(3):
    print(values[x])
    top3 = top3 + values[x]


print(top3)