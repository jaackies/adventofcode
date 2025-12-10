import sys

dial = 50
password = 0
for line in sys.stdin:
  line = line.strip()
  turn = int(line[1:]) if line[0] == "L" else -1*int(line[1:])
  dial = (dial + turn)%100
  if dial == 0: password+=1

print(password)