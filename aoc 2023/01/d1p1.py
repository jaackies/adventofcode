# read input line by line
# 
# do the coe\
import sys

sum = 0

for line in sys.stdin:
  line = line.strip()
  length = len(line)
  i = 0
  first = False
  last = False
  print(line)
  while (not(first and last)):
    if (line[i].isnumeric() and not first):
      sum+= int(line[i])*10
      print(int(line[i])*10)
      first = True
    if (line[length-1-i].isnumeric() and not last):
      sum+= int(line[length-1-i])
      print(int(line[length-1-i]))
      last = True
    i+=1
  print("------")
  # for i in range(0, length):
  #   if (line[i].isnumeric() && !first):
  #     sum += line[i]*10
  #     first = True
  #   if(line[length-1-i].isnumeric() && !last):
  #     sum+= line[length-1-i]
  #     last = True
    
print(sum)