"""
openent:
a is rock
b is paper
c is scissors

me:
x is rock
y is paper
z is scissors
"""

choiceVal = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}

def didIWin(opchoice, mychoice):
    ## Returns 0 for loss, 3 for draw and 6 for win ##
    match opchoice:
        case "A":
            match mychoice:
                case "X": return 3
                case "Y": return 6
                case "Z": return 0
        case "B":
            match mychoice:
                case "X": return 0
                case "Y": return 3
                case "Z": return 6
        case "C":
            match mychoice:
                case "X": return 6
                case "Y": return 0
                case "Z": return 3


def calcScore(op,mc):
    return choiceVal[mc] + didIWin(op,mc)

## get the input from the challenge ##
plays = []
with open("day2input.txt", "r") as f:
    for line in f.readlines():
        plays.append((line.split()))

totscore = 0
for play in plays:
    totscore += calcScore(*play)

print(totscore)

## Part 2 ##

mapping = {"X":0, "Y":3, "Z":6}

def pickMove(opchoice, reqresult):
    ## Returns 0 for loss, 3 for draw and 6 for win ##
    match opchoice:
        case "A":
            match reqresult:
                case 3: return "X"
                case 6: return "Y"
                case 0: return "Z"
        case "B":
            match reqresult:
                case 0: return "X"
                case 3: return "Y"
                case 6: return "Z"
        case "C":
            match reqresult:
                case 6: return "X"
                case 0: return "Y"
                case 3: return "Z"

totscore2 = 0
for play in plays:
    play[1] = mapping[play[1]]
    mychoice = pickMove(play[0], play[1])
    totscore2 += (choiceVal[mychoice] + play[1])

print(totscore2)


