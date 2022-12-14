with open("day7input.txt", "r") as f:
    theinput = f.read().splitlines()

## eg: {"a":2355, "b":3453)} ##
dirtotals = {}

## eg: [("a","b","c"), ("x", "y", "z")]
subdirs = []


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
    dirtotals[currdir] = total


lslines = []
## first dir should be root, /
currdir = theinput[0][5:]
for line in theinput:
    if "$" in line:
        if "cd" in line:
            ## If we are going back 1 level
            if ".." in line:
                ## Find the directory containing the current directory ##
                for dir in subdirs:
                    if currdir in dir[1:]:
                        prevdir: str = dir[0]
                ## Change the current directory to the previous one ###
                currdir = prevdir
            addUp()
            currdir = line[5:]
            lslines = []
        elif "ls" in line:
            continue
    else:
        ## If this is the output from an ls command, add it too the list
        lslines.append(line)

print(dirtotals)
print(subdirs)
