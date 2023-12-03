import sys

# pushups done: 11

rows = 0
cols = 0
marking_matrix = []
part_matrix = []

def populate():
  row = 0
  for line in sys.stdin:
    line = line.rstrip()
    length = len(line)
    marking_matrix.append([0]*length)
    part_matrix.append([-1]*length)
    for i in range(length):
      if line[i].isnumeric():
        part_matrix[row][i] = int(line[i])
      elif (line[i] != "."): 
        marking_matrix[row][i] = 2
    row += 1
  global rows, cols
  rows = row
  cols = len(part_matrix[0])

def mark_helper(x, y):
  if part_matrix[x][y] != -1:
    marking_matrix[x][y] = 1
    if (y-1 < cols and marking_matrix[x][y-1] != 1):
      mark_helper(x,y-1)
    if (y+1 < cols and marking_matrix[x][y+1] != 1):
      mark_helper(x,y+1)

def mark():
  x, y = (0, 0)
  for x in range(rows):
    for y in range(cols):
      if (marking_matrix[x][y] == 2):
        mark_helper(x-1,y-1)
        mark_helper(x-1,y)
        mark_helper(x-1,y+1)
        mark_helper(x,y-1)
        mark_helper(x,y+1)
        mark_helper(x+1,y-1)
        mark_helper(x+1,y)
        mark_helper(x+1,y+1)

def sum_helper(x, y):
  sum = part_matrix[x][y]
  marking_matrix[x][y] = 0
  y+=1
  while (y < cols and marking_matrix[x][y] == 1):
    sum *= 10
    marking_matrix[x][y] = 0
    sum += part_matrix[x][y]
    y += 1
  return sum

def solution():
  x, y = (0, 0)
  sum = 0
  for x in range(rows):
    for y in range(cols):
      if (marking_matrix[x][y] == 1 and part_matrix[x][y] != 0):
        sum += sum_helper(x, y)
  return sum

populate()
mark()
print(solution())