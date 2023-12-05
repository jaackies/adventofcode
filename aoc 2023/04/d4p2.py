import sys

# pushups done: none :) !

winning = None
pile = None
points = 0

lines = sys.stdin.readlines()

cardpile = [1] * len(lines)
pilemarker = -1

for line in lines:
    pilemarker += 1
    line = line.strip("Card :").strip().split("|")
    for nums in line:
        nums = nums.split()
        if nums[0][-1] == ":":
            winning = set(nums[1:])
        else:
            pile = set(nums)
            numwinners = len(pile.intersection(winning))
            #now we process the copies
            for i in range(1,numwinners+1):
                cardpile[pilemarker+i] += 1*cardpile[pilemarker]

print(sum(cardpile))