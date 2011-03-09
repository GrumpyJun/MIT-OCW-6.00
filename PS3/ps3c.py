from string import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print ('breaking key ' + str(key) +' into ' + str(key1) + " " + str(key2))
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print( 'match1',match1)
        print( 'match2',match2)
        print( 'possible matches for',key1,key2,'start at',filtered)
        print()
        print()
    return allAnswers

def constrainedMatchPair(firstMatch, secondMatch, length):
	tuple = ()
	for first_value in firstMatch:
		for second_value in secondMatch:
			if(first_value + length + 1 == second_value):
				tuple += (first_value,)
	return tuple

def subStringMatchExact(target, key):
	str_index = 0
	match_pos = 0
	count = 0
	no_match = 0
	tuple = ()

	while(no_match == 0):
		pos = target[str_index:].find(key) + 1

		if(pos == 0 or str_index >= len(target)):
			no_match = 1
		else:
			tuple += (str_index + pos - 1,)
			count += 1

		str_index += pos

	return tuple

print(subStringMatchOneSub(key10, target1))
print(subStringMatchOneSub(key12, target1))
print(subStringMatchOneSub(key13, target2))
