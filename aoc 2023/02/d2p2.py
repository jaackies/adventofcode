import sys

games = []
# {red,
# green,
# blue}

for game in sys.stdin:
  counter = 0
  store = 0
  storage = [0,0,0]
  game = game.strip().split(" ")
  for word in game:
    if (counter < 2):
      counter+=1
      continue
      #skips game and game id
    if word.isnumeric():
      store = int(word)
    else:
      if (word[0] == "r" and store > storage[0]):
        storage[0] = store
      elif (word[0] == "g" and store > storage[1]):
        storage[1] = store
      elif (word[0] == "b" and store > storage[2]):
        storage[2] = store
  games.append(storage)

def solution():
  sum = 0
  for game in games:
    sum += (game[0] * game[1] * game[2])
  return sum

print(solution())