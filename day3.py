from string import ascii_lowercase, ascii_uppercase
priorities = list(ascii_lowercase + ascii_uppercase)

with open("inputs/day3input.txt", "r") as f:
    bags = f.read().splitlines()

def addUp(lis):
    total = 0
    for li in lis:
        total += (priorities.index(li) + 1)
    return total

intersections = []
for bag in bags:
    sec1, sec2 = bag[:len(bag) // 2], bag[len(bag) // 2:]
    intersections += list(set(sec1).intersection(set(sec2)))[0]

print(addUp(intersections))

## part 2 ##
intersections2 = []
for i in range(0, len(bags), 3):
    b1, b2, b3 = bags[i:i + 3]
    intersections2 += list((set(b1).intersection(set(b2), set(b3))))[0]

print(addUp(intersections2))
