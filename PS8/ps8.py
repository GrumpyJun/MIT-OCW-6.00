# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    subject_dict = {}

    my_file = open(filename)

    # Iterate over each line, creating the dictionary as you go.
    for line in my_file.readlines():
        subject_name, subject_value, subject_work = line.split(',')
        subject_dict[subject_name] = (int(subject_value), int(subject_work))

    my_file.close()

    return subject_dict

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    totalWorkSoFar = 0
    solved_dict = {}
    currentBestClass = "0.00"

    # Loop while we are still finding valid classes to add
    while totalWorkSoFar <= maxWork and currentBestClass != None:
        currentBestClass = None

        # Find the class with the most value that doesn't
        # put us over the max work constraint
        for key in subjects.keys():

            # If we already have this class, skip it this time around
            if key in solved_dict.keys():
                continue

            # If we haven't found a valid class yet, the only constraint is
            # that it doesn't go over the maxWork constraint
            if currentBestClass == None:

                if totalWorkSoFar + subjects[key][WORK] <= maxWork:
                    currentBestClass = key

            # Otherwise we have found a valid class, and must determine
            # if the current class is better per the comparator function
            else:
                # If it doesn't exceed maxWork and it's better than the
                # current, make it the new current best
                if totalWorkSoFar + subjects[key][WORK] <= maxWork and comparator(subjects[key], subjects[currentBestClass]):
                    currentBestClass = key

        if currentBestClass != None:
            solved_dict[currentBestClass] = (subjects[currentBestClass][0], subjects[currentBestClass][1])
            totalWorkSoFar = totalWorkSoFar + solved_dict[currentBestClass][WORK]

    return solved_dict

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    subj_dict = loadSubjects(SUBJECT_FILENAME)

    for i in range(1, 12):
        start_time = time.time()

        solved_dict = bruteForceAdvisor(subj_dict, i)

        end_time = time.time()

        print(solved_dict)

        total_time = end_time - start_time

        print("maxWork: %d" % i)
        print("%0.2f seconds" % total_time)
        print()

# Problem 3 Observations
# ======================
#
#{'7.17': (10, 1)}
#maxWork: 1
#0.00 seconds
#
#{'6.00': (10, 1), '7.17': (10, 1)}
#maxWork: 2
#0.01 seconds
#
#{'6.00': (10, 1), '7.16': (7, 1), '7.17': (10, 1)}
#maxWork: 3
#0.03 seconds
#
#{'6.00': (10, 1), '7.16': (7, 1), '7.17': (10, 1), '12.04': (7, 1)}
#maxWork: 4
#0.09 seconds
#
#{'15.01': (7, 1), '6.00': (10, 1), '7.16': (7, 1), '7.17': (10, 1), '12.04': (7, 1)}
#maxWork: 5
#0.28 seconds
#
#{'7.16': (7, 1), '7.17': (10, 1), '7.00': (7, 1), '6.00': (10, 1), '12.04': (7, 1), '15.01': (7, 1)}
#maxWork: 6
#0.85 seconds
#
#{'7.16': (7, 1), '7.17': (10, 1), '7.00': (7, 1), '6.00': (10, 1), '24.12': (6, 1), '12.04': (7, 1), '15.01': (7, 1)}
#maxWork: 7
#2.47 seconds
#
#{'7.16': (7, 1), '7.17': (10, 1), '7.00': (7, 1), '6.00': (10, 1), '24.12': (6, 1), '12.04': (7, 1), '15.01': (7, 1), '2.03': (6, 1)}
#maxWork: 8
#7.03 seconds
#
#{'7.16': (7, 1), '7.17': (10, 1), '7.00': (7, 1), '6.00': (10, 1), '24.12': (6, 1), '7.18': (10, 2), '12.04': (7, 1), '15.01': (7, 1)}
#maxWork: 9
#18.64 seconds
#
#{'7.16': (7, 1), '7.17': (10, 1), '7.00': (7, 1), '6.00': (10, 1), '24.12': (6, 1), '7.18': (10, 2), '12.04': (7, 1), '15.01': (7, 1), '2.03': (6, 1)}
#maxWork: 10
#49.76 seconds
#
#{'7.16': (7, 1), '7.17': (10, 1), '7.00': (7, 1), '6.00': (10, 1), '24.12': (6, 1), '7.18': (10, 2), '12.04': (7, 1), '15.01': (7, 1), '22.03': (10, 2)}
#maxWork: 11
#125.49 seconds


#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    classnames = list(subjects.keys())
    mem = {}
    solutions = dpMax(subjects, classnames, len(subjects) - 1, maxWork, mem)
    print(solutions)

def dpMax(subjects, classnames, i, availWork, mem):
    local_mem = {}

    # If we've seen this before, just use the stored value
    if (i, availWork) in mem.keys():
        return mem[(i, availWork)]
    
    # If this is the last node, it must return either work or 0, because
    # we can either take the class or not take the class
    if i == 0:
        if subjects[classnames[i]][WORK] <= availWork:
            local_mem = (subjects[classnames[i]][VALUE], [classnames[i]])
            mem[(i, availWork)] = local_mem
            return local_mem
        else:
            local_mem = (0, [])
            mem[(i, availWork)] = local_mem
            return local_mem

    without_i = dpMax(subjects, classnames, i - 1, availWork, mem)

    # If we don't have enough available work to include the current node,
    # don't take that path
    if subjects[classnames[i]][WORK] > availWork:
        mem[(i, availWork)] = without_i
        return without_i
    else:
        with_i    = dpMax(subjects, classnames, i - 1, availWork - subjects[classnames[i]][WORK], mem)
        with_i_value = with_i[0] + subjects[classnames[i]][VALUE]
        with_i_bests = with_i[1][:]
        with_i_bests.append(classnames[i])

    if without_i[0] >= with_i_value:
        mem[(i, availWork)] = without_i
        return without_i
    else:
        mem[(i, availWork)] = (with_i_value, with_i_bests)
        return (with_i_value, with_i_bests)

#(0, [])
#maxWork: 0  0.00000 seconds
#(10, ['7.17'])
#maxWork: 1  0.00000 seconds
#(20, ['7.17', '6.00'])
#maxWork: 2  0.00000 seconds
#(27, ['7.16', '7.17', '6.00'])
#maxWork: 3  0.01000 seconds
#(34, ['7.16', '7.17', '12.04', '6.00'])
#maxWork: 4  0.00000 seconds
#(41, ['7.16', '7.17', '12.04', '15.01', '6.00'])
#maxWork: 5  0.00000 seconds
#(48, ['7.16', '7.17', '12.04', '15.01', '6.00', '7.00'])
#maxWork: 6  0.00000 seconds
#(54, ['7.16', '7.17', '24.12', '12.04', '15.01', '6.00', '7.00'])
#maxWork: 7  0.00000 seconds
#(60, ['7.16', '7.17', '24.12', '12.04', '15.01', '6.00', '7.00', '2.03'])
#maxWork: 8  0.01300 seconds
#(64, ['7.16', '7.17', '24.12', '7.18', '12.04', '15.01', '6.00', '7.00'])
#maxWork: 9  0.00400 seconds
#(70, ['7.16', '7.17', '24.12', '7.18', '12.04', '15.01', '6.00', '7.00', '2.03'])
#maxWork: 10  0.00500 seconds
#(74, ['7.16', '7.17', '24.12', '7.18', '12.04', '15.01', '22.03', '6.00', '7.00'])
#maxWork: 11  0.00500 seconds


#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    #subj_dict = loadSubjects("test_input_dp.txt")
    subj_dict = loadSubjects(SUBJECT_FILENAME)

    for i in range(0, 12):
        start_time = time.time()

        dpAdvisor(subj_dict, i)

        end_time = time.time()

        total_time = end_time - start_time

        print("maxWork:", str(i), " %0.5f seconds" % total_time)

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

if __name__ == '__main__':
    #loadSubjects(SUBJECT_FILENAME)
    #bruteForceTime()
    dpTime()
