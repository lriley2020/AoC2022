with open("inputs/day7input.txt", "r") as f:
    theinput = f.read().splitlines()

## eg: {"a":2355, "b":3453)} ##
dirtotals = {}

## eg: [("a","b","c"), ("x", "y", "z")]
subdirs = []

def addUp():
    subs = [currdir]
    total = 0
    print(lslines)
    for line in lslines:
        if "dir" in line:
            subs.append(line[4:])
        else:
            size = ""
            for char in line:
                if char.isnumeric():
                    size += char
            total += int(size)
    dirtotals[currdir] = total
    subdirs.append(tuple(subs))


lslines = []
## first dir should be root, /
currdir = "/"
linenum = 0
for line in theinput:
    if "$" in line:
        if "cd" in line:
            if lookForEndOfLs:
                addUp()
                lookForEndOfLs = False
            if ".." in line:
                ## Find the directory containing the current directory ##
                for dir in subdirs:
                    if currdir in dir[1:]:
                        prevdir = dir[0]
                ## Change the current directory to the previous one ###
                currdir = prevdir
            else:
                currdir = line[5:]
        elif "ls" in line:
            lookForEndOfLs = True
            lslines = []
    else:
        ## If this is the output from an ls command, add it too the list
        lslines.append(line)
addUp()

print(dirtotals)
print()
print(subdirs)
