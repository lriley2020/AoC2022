with open("day5input.txt", "r") as f:
    theinput = f.readlines()

columns = {}
moves = []
for line in theinput:
    if not any([char.isdigit() for char in line]):
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


print(columns)
print(moves)