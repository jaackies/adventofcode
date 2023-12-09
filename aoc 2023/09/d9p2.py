import sys

#pushup counter: | (i changed too many += into -=s)

def zerocheck(nums):
    for num in nums:
        if num != 0:
            return False
    return True

def difference(nums):
    final = 0
    diff = []
    for i in range(1, len(nums)):
        diff.append((nums[i])-(nums[i-1]))
    if (zerocheck(diff)):
        return 0
    else:
        final -= diff[0]
        final -= difference(diff)
        return final

def solution():
    sol = 0
    for line in sys.stdin:
        line = line.strip().split()
        line = list(map(int, line))
        sol += line[0]
        sol += difference(line)
    return sol

print(solution())