import sys

result = 0
for line in sys.stdin:
  print("new line :3")
  pospos = [] #keep track of possible positions
  start = 0
  pos = line.find("mul(", start)
  while (pos!=-1):
    pospos.append(pos)
    start += pos+1
    pos = line.find("mul(", start)
  for pos in pospos:
    # check if true, and then store result if true
    i = 4 # where 0th index is pos, we start from index 4 (after "mul(")
    subline = line[pos:pos+13]
    a = 0
    b = 0
    alimit = 3
    blimit = 3
    print(pos, ":", subline)
    while True:
      if (subline[i].isnumeric() and alimit > 0):
        a = a*10 + int(subline[i])
        print("a:", a)
        alimit -= 1
        i+=1
        continue
      if (subline[i] != "," and alimit>-1):
        print(subline[i],"NOT COMMA")
        # a = 0
        break
      # is a comma
      if (subline[i] == ","):
        alimit = -1
        i+=1
        continue
      if (subline[i].isnumeric() and blimit > 0):
        b = b*10 + int(subline[i])
        print("b:",b)
        blimit -= 1
        i+=1
        continue
      if (subline[i] != ")"):
        print(subline[i],"NOT BRACKET")
        # b = 0
        break
      if (subline[i] == ")"):
        result += a*b
        print("i did a multiply")
        break
  break # for testing
print(result)

# answer is too low 1236709
# issue appears to be in having issues with str.find
# 
# also this one V not sure if i did math wrong, added an extra 1 in code but haven't checked yet lol
# 1861 : mul(144,160
# a: 1
# a: 14
# a: 144
# b: 1
# b: 16
# b: 160
#   NOT BRACKET