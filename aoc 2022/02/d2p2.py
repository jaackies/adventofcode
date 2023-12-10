import sys

# A = rock, B = paper, C = scissors
# X = lose, Y = draw, Z = win
# rock = 1, paper = 2, scissors = 3
# lost = 0, draw = 3, win = 6

def outcome(opp, you):
    points = 0
    match (opp):
        case "A":
            if you == "X":
                points += 3
            elif you == "Y":
                points += 4
            else:
                points += 8
        case "B":
            if you == "X":
                points += 1
            elif you == "Y":
                points += 5
            else:
                points += 9
        case "C":
            if you == "X":
                points += 2
            elif you == "Y":
                points += 6
            else:
                points += 7
    return points

def solution():
    sol = 0
    for line in sys.stdin:
        line = line.strip().split()
        sol += outcome(line[0], line[1])
    return sol

print(solution())