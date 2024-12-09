import sys

safe_sum = 0
for report in sys.stdin:
  report = [int(x) for x in report.strip().split()]
  prev = report[0]
  inc = 1 if (prev<report[1]) else -1
  safe = True
  for level in report[1:]:
    level = level
    diff = (level-prev)*inc
    if ((diff < 1) or (diff > 3)):
      safe = False
      break
    prev = level
  if safe:
    safe_sum+=1
print(safe_sum)