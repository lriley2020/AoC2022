with open("day7input.txt", "r") as f:
    theinput = f.read().splitlines()


## eg: [("a",2355), ("b",3453)] ##
dirtotals = []

## eg: {"a":["b","x"], "b":["c","d"]}
subdirs = {}

def addUp():
    subdirs[currdir] = []
    total = 0
    for line in lslines:
        if "dir" in line:
            subdirs[currdir].append(line[4:])
        else:
            size = ""
            for char in line:
                if char.isnumeric():
                    size += char
            total += int(size)
    dirtotals.append((currdir,total))


lslines = []
currdir = theinput[0][5:]
for line in theinput:
    if "$" in line:
        lslines = []
        if "cd" in line:
            addUp()
            currdir = line[5:]
        elif "ls" in line:
            continue
    lslines.append(line)

print(dirtotals)
print(subdirs)