# Problem Set 4
# Name: 
# Collaborators: 
# Time: 

#
# Problem 1
#

from math import *

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    total = []

    for i in range(years):
        if(i == 0):
            total.append(salary * save * .01)
        else:
            total.append(total[i-1] * (1 + .01 * growthRate) + salary * save * .01)

    return total

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (str(savingsRecord))
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

    total = []

    for i in range(len(growthRates)):
        if(i == 0):
            total.append(salary * save * .01)
        else:
            total.append(total[i-1] * (1 + .01 * growthRates[i]) + salary * save * .01)

    return total

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print (str(savingsRecord))
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    
    total = []

    for i in range(len(growthRates)):
        if(i == 0):
            total.append(savings * (1 + .01 * growthRates[i]) - expenses)
        else:
            total.append(total[i-1] * (1 + .01 * growthRates[i]) + - expenses)

    return total

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (str(savingsRecord))
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    preRetireAmounts = nestEggVariable(salary, save, preRetireGrowthRates)
    savings = preRetireAmounts[len(preRetireGrowthRates) - 1]

    bs_low = 0
    bs_high = savings
    bs_current = bs_high / 2.0
    
    print("Binary Search: " + str(bs_current))
    postRetireAmounts = postRetirement(savings, postRetireGrowthRates, bs_current)
    while(abs(postRetireAmounts[len(postRetireGrowthRates) - 1]) > epsilon):
        if postRetireAmounts[len(postRetireGrowthRates) - 1] > 0:
            bs_low = bs_current
        else:
            bs_high = bs_current

        bs_current = ((bs_high - bs_low) / 2) + bs_low
        print("Binary Search: " + str(bs_current))

        postRetireAmounts = postRetirement(savings, postRetireGrowthRates, bs_current)

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print (str(expenses))
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.


testNestEggFixed()
testNestEggVariable()
testPostRetirement()
testFindMaxExpenses()
