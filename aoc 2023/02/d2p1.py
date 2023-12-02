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

#which games possible if 12 red, 13 green, 14 blue
#sum those ids up

def solution(red, green, blue):
  possiblesum = 0
  i = 0
  for game in games:
    i += 1
    if (game[0] > red):
      continue
    if (game[1] > green):
      continue
    if (game[2] > blue):
      continue
    possiblesum += i
  print(possiblesum)

solution(12,13,14)