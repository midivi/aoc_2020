with open("../input/day6_1.txt") as f:
    lines = f.read()

groups = lines[0:-1].split('\n\n')  # Don't include last newline character

num_questions = 0
for group in groups:
    questions = group.replace('\n', '')
    num_questions += len(set(questions))

print(num_questions)

# Part 2

num_questions = 0
for group in groups:
    subgroups = group.split('\n')
    questions = set(subgroups[0])
    for subgroup in subgroups[1::]:
        questions &= set(subgroup)
    num_questions += len(questions)

print(num_questions)
