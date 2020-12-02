f = open("../input/day2_1.txt")
lines = list(f.readlines())


def process_line(line):
    rule, letter, password = line.strip().replace(':', '').split()
    rule_min = int(rule.split('-')[0])
    rule_max = int(rule.split('-')[1])
    return rule_min, rule_max, letter, password


def correct_entry(rule_min, rule_max, letter, password):
    if rule_min <= password.count(letter) <= rule_max:
        return True
    return False

entries = list(map(lambda l: correct_entry(*process_line(l)), lines[0:-1]))

print(entries.count(True))

def correct_entry_part_2(idx_1, idx_2, letter, password):
    idx_1 -= 1
    idx_2 -= 1
    cond1 = password[idx_1] == letter
    cond2 = password[idx_2] == letter
    return [cond1, cond2].count(True)  == 1

entries = list(map(lambda l: correct_entry_part_2(*process_line(l)), lines[0:-1]))

print(entries.count(True))
