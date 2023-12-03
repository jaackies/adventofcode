import sys

elves = []
calsum = 0
for line in sys.stdin:
    line = line.rstrip()
    if line.isnumeric():
        calsum += int(line)
    else:
        elves.append(calsum)
        calsum = 0
# to acount for the final elf
elves.append(calsum)

elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])
