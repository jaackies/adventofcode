import sys

# pushups done: || + ||| for cringefail reading comp

winning = None
pile = None
points = 0

for line in sys.stdin:
    line = line.strip("Card :").strip().split("|")
    for nums in line:
        nums = nums.split()
        if nums[0][-1] == ":":
            winning = set(nums[1:])
        else:
            pile = set(nums)
            numwinners = len(pile.intersection(winning))
            if numwinners == 1:
                points += 1
            elif numwinners > 1:
                points += (2**(numwinners-1))

print(points)