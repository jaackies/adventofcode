import sys

sum = 0
reference = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def takefirst(elem):
  return elem[0]


# returns tuple of tuples((first,digit),(last,digit))
# internal tuple is (location, corresponding digit)
def findwords(dictionary, line):
  list = []
  for key in dictionary.keys():
    index = line.find(key)
    if(index != -1):
      list.append((index, dictionary[key]))
    index = line.rfind(key)
    if (index != -1):
      list.append((index, dictionary[key]))
  if len(list) == 0:
    return -1, -1
  list.sort(key=takefirst)
  return (list[0],list[-1])
  # return the foremost and lastmost - will need to find

for line in sys.stdin:
  line = line.strip()
  length = len(line)
  print(line)
  firstref, lastref = findwords(reference, line)
  i = 0
  first = False
  last = False
  while (not(first and last)):
    if (line[i].isnumeric() and not first):
      if (firstref != -1 and firstref[0] < i):
        num = firstref[1] 
      else:
        num = int(line[i])
      sum += num*10
      print(num*10)
      first = True
    if (line[length-1-i].isnumeric() and not last):
      if (lastref != -1 and lastref[0] > (length-1-i)):
        num = lastref[1]
      else:
        num = int(line[length-1-i])
      sum += num
      print(num)
      last = True
    i+=1
  print("------")

print(sum)