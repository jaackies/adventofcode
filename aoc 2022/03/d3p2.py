import sys
import string

def alphconvert(letter):
	if letter.isupper():
		return ord(letter)-38
	else:
		return ord(letter)-96

def solution():
	sum = 0
	while(True):
		first = set(sys.stdin.readline().strip())
		second = set(sys.stdin.readline().strip())
		third = set(sys.stdin.readline().strip())
		if first == set():
			break
		shared = first.intersection(second).intersection(third)
		sum += alphconvert(max(shared))
	return sum

print(solution())