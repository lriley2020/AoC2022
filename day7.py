with open("day7input.txt", "r") as f:
    theinput = f.read().splitlines()

## eg: {"a":2355, "b":3453)} ##
dirtotals = {}

## eg: [("a","b","c"), ("x", "y", "z")]
subdirs = []

def addUp():
    print(f"Adding up directory {currdir}")
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
    print(f"About to commit, input line number {linenum}, total for this directory is {total}")
    print()
    dirtotals[currdir] = total
    subdirs.append(tuple(subs))


lslines = []
## first dir should be root, /
currdir = "/"
linenum = 0
for line in theinput:
    linenum += 1
    #print(f"Input line number {linenum}, current directory is {currdir}")
    ## Is this a command? ##
    if "$" in line:
        if "cd" in line:
            if lookForEndOfLs:
                addUp()
                lookForEndOfLs = False
            if ".." in line:
                print(f"Going backwards, input line number {linenum}")
                ## Find the directory containing the current directory ##
                for dir in subdirs:
                    if currdir in dir[1:]:
                        prevdir = dir[0]
                ## Change the current directory to the previous one ###
                print(f"The previous directory to {currdir} is {prevdir}")
                currdir = prevdir
            else:
                ## If we are not changing to an outer directory, change to the next one ##
                currdir = line[5:]
        elif "ls" in line:
            lookForEndOfLs = True
            lslines = []
    else:
        ## If this is the output from an ls command, add it too the list
        lslines.append(line)
addUp()

print()
print(dirtotals)
print()
print(subdirs)
