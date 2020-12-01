f = open("../input/day1_1.txt")
lines = f.readlines()
entries = list(map(lambda line: int(line.strip()), lines[0:-1]))

answer = set([
    a * b
    for a in entries
    for b in entries
    if a + b == 2020
])

print(list(answer)[0])

answer = set([
    a * b * c
    for a in entries
    for b in entries
    for c in entries
    if a + b + c == 2020
])

print(list(answer)[0])
