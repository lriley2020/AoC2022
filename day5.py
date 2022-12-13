### This still doesn't work yet! ###

with open("day5input.txt", "r") as f:
    theinput = f.readlines()

columns = {}
moves = []
for line in theinput:
    if not any([char.isdigit() for char in line]) and line != "\n":
        count = 0
        for i in range(1, 34, 4):
            count += 1
            if line[i] != " ":
                if count not in columns:
                    columns[count] = [line[i]]
                else:
                    columns[count].append(line[i])
    else:
        if "move" in line:
            steps = []
            for char in line:
                if char.isdigit():
                    steps.append(int(char))
            moves.append(steps)


result = '\n'.join(
  f'{key}: {value}' for key, value in sorted(columns.items())
)
print(result)

for move in moves[:1]:
    items = move[0]
    startstack = move[1]
    endstack = move[2]
    copied = columns[startstack][:items]
    del columns[startstack][:items]
    copied.reverse()
    columns[endstack] = [*copied, *columns[endstack]]


print()
result = '\n'.join(
  f'{key}: {value}' for key, value in sorted(columns.items())
)
print(result)


#thecode = ""
#for column in columns.values():
#    thecode += column[-1]
#print(thecode)
