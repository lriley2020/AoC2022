with open("inputs/day4input.txt", "r") as f:
    theinput = f.read().splitlines()

pairs = []
for line in theinput:
    pair = line.split(",")
    parsedpair = []
    for elf in pair:
        parsedpair.append(tuple((map(int, elf.split("-")))))
    pairs.append(tuple(parsedpair))

count = 0
for pair in pairs:
    elf1range = range(pair[0][0], pair[0][1] + 1)
    elf2range = range(pair[1][0], pair[1][1] + 1)
    if all(e in elf1range for e in elf2range) or all(e in elf2range for e in elf1range):
        count += 1

print(count)

## Part 2 ##
count2 = 0
for pair in pairs:
    elf1range = range(pair[0][0], pair[0][1] + 1)
    elf2range = range(pair[1][0], pair[1][1] + 1)
    if set(elf1range).intersection(set(elf2range)):
        count2 += 1

print(count2)
