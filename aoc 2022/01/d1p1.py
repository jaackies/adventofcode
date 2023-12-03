import sys

# goal: find elf with the most calories and return how many calories they're carrying

most = 0
calsum = 0
for line in sys.stdin:
    line = line.rstrip()
    if line.isnumeric():
        calsum += int(line)
    else:
        if calsum > most:
            most = calsum
        calsum = 0

print(most)
