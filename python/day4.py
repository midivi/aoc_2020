with open("../input/day4_1.txt") as f:
    lines = f.readlines()

PASSPORT_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
]
password_seperator = '\n'

passports = 0
passport = {}
for line in lines:
    if line == password_seperator:
        if set(passport.keys()) == set(PASSPORT_FIELDS):
            passports += 1
        elif set(passport.keys()) == set(PASSPORT_FIELDS) - set(['cid']):
            passports += 1
        passport = {}
        continue
    for field in set(PASSPORT_FIELDS) - passport.keys():
        if field in line:
            passport[field] = True

print(passports)

# Part 2 no fun :(
