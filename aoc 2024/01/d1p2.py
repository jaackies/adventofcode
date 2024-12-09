import sys

#this is jank i'm sorry

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
(l,r) = (0,0)
scoring = None #currently scoring for this value
score = 0
while (l < len(left)):
  scoring = left[l]
  while ((r < len(right)) and (right[r] < scoring)):
    r+=1
  while ((r < len(right)) and (right[r] == scoring)):
    score+=1
    r+=1
  to_score = 0
  while ((l < len(left)) and (left[l] == scoring)):
    to_score+=1
    l+=1
  score *= to_score
  score *= scoring
  sum += score
  score = 0

print(sum)