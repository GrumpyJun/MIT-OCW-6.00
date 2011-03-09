from string import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def countSubStringMatch(target, key):
	str_index = 0
	match_pos = 0
	count = 0
	no_match = 0

	while(no_match == 0):
		pos = target[str_index:].find(key) + 1
		str_index += pos
		if(pos == 0):
			no_match = 1
		else:
			count += 1

	return count

def countSubStringMatchRecursive(target, key):
	str_index = target.find(key) + 1

	if(str_index == 0):
		return 0
	else:
		return 1 + countSubStringMatchRecursive(target[str_index:], key)

nonRecurCount = 0
nonRecurCount = countSubStringMatch(target1, key10)
print("Iterative version found " + str(nonRecurCount) + " matches.")

recurCount = 0
recurCount = countSubStringMatchRecursive(target1, key10)
print("Recursive version found " + str(recurCount) + " matches.")
