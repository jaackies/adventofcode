import sys
import string

def alphconvert(letter):
	if letter.isupper():
		return ord(letter)-38
	else:
		return ord(letter)-96

def solution():
	sum = 0
	for line in sys.stdin:
		line = line.strip()
		halfway = int(len(line)/2)
		first = set(line[:halfway])
		second = set(line[halfway:])
		shared = first.intersection(second)
		sum += alphconvert(max(shared))
	return sum

print(solution())