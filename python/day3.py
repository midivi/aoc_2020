from itertools import cycle

f = open("../input/day3_1.txt")
lines = f.readlines()


def process_line(line):
    return line.strip()


def skip(n, indexes):
    for _ in range(n):
        next(indexes)


processed_lines = list(map(process_line, lines))

indexes = cycle(range(0, len(processed_lines[0])))


def recurse(slope_x, slope_y, lines, trees, indexes):
    if not len(lines):
        return trees
    idx = next(indexes)
    skip(slope_x - 1, indexes)
    if lines[0][idx] == '#':
        trees += 1
    return recurse(slope_x, slope_y, lines[slope_y::], trees, indexes)


# Part 1
print(recurse(3, 1, processed_lines, 0, indexes))


# Part 2
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

result = 1
for (slope_x, slope_y) in slopes:
    indexes = cycle(range(0, len(processed_lines[0])))
    result *= recurse(slope_x, slope_y, processed_lines, 0, indexes)

print(result)
