from string import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExact(target, key):
	str_index = 0
	match_pos = 0
	count = 0
	no_match = 0
	tuple = ()

	while(no_match == 0):
		pos = target[str_index:].find(key) + 1

		if(pos == 0):
			no_match = 1
		else:
			tuple += (str_index + pos - 1,)
			count += 1

		str_index += pos

	return tuple

print("Tuple for target 1, key10: " + str(subStringMatchExact(target1, key10)))
print("Tuple for target 1, key13: " + str(subStringMatchExact(target1, key13)))
