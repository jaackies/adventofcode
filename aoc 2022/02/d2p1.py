import sys

# A = rock, B = paper, C = scissors
# X = rock, Y = paper, Z = scissors
# rock = 1, paper = 2, scissors = 3
# lost = 0, draw = 3, win = 6

def outcome(opp, you):
    points = 0
    match (opp):
        case "A":
            if you == "Y":
                points += 6
            elif you == "X":
                points += 3
        case "B":
            if you == "Z":
                points += 6
            elif you == "Y":
                points += 3
        case "C":
            if you == "X":
                points += 6
            elif you == "Z":
                points += 3
        # case other:
            # break
    match (you):
        case "X":
            points += 1
        case "Y":
            points += 2
        case "Z":
            points += 3
        # case other:
            # break
    return points

def solution():
    sol = 0
    for line in sys.stdin:
        line = line.strip().split()
        sol += outcome(line[0], line[1])
    return sol

print(solution())   