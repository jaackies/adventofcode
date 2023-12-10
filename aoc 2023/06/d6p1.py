import sys
import math

# pushups to do:

data = []

#solves for first x
def formula(t, r):
  # a = -1, b = t, c = r
  x = ((-t)-math.sqrt((t**2)-(-4*r)))/(-2)
  return x

# inside is tuples where [0] = time, [1] = distance

time = sys.stdin.readline().strip().split()
distances = sys.stdin.readline().strip().split()

# populate data
for i in range (1, len(time)):
  data.append((time[i],distances[i]))

print(formula (7, 9))