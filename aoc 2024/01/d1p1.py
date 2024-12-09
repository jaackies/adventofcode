import sys

left = []
right = []
for line in sys.stdin:
  line = line.strip().split()
  # populate two lists
  (l,r) = line
  left.append(int(l))
  right.append(int(r))

left.sort()
right.sort()

sum = 0
for i in range(0,len(left)):
  sum += abs(left[i]-right[i])

print(sum)