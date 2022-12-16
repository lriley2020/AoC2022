elves = []

def addUp(*meals):
    return sum(*meals)

with open("inputs/day1input.txt", "r") as f:
    newelf = []
    for line in f.readlines():
        if len(line.strip()) == 0:
            elves.append(newelf)
            newelf = []
        else:
            newelf.append(int(line.strip()))

elvestotal = list(map(addUp, elves))
print(max(elvestotal))

### Part 2 ###

elvestotal.sort(reverse=True)
print(sum(elvestotal[:3]))