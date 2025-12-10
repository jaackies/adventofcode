import sys

dial = 50
password = 0
for line in sys.stdin:
  line = line.strip()
  direction = -1 if line[0] == "L" else 1 # if moving R
  turn = int(line[1:])*direction
  # o_pw = password
  password += turn//(100*direction)
  rem = turn % (100*direction)
  if direction == -1: # going left
    if rem <= -1*dial and dial != 0: password+=1
  else: # going right
    if rem >= (100-dial): password+=1
  # o_dial = dial
  dial = (dial + turn)%100
  # if o_pw != password:
    # print(f"dial @ {o_dial} -> {dial} \t password at {password} \t after turn {turn}")

print(password)