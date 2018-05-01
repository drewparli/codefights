"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""

def allLongestStrings(inputArray):
    cost = list(map(len, inputArray))
    longest = max(cost)
    _,result = zip(*filter(lambda n : n[0] == longest, zip(cost, inputArray)))
    return(result)



if __name__ == '__main__':
    inputArray = ["aba", "aa", "ad", "vcd", "aba"]
    print(allLongestStrings(inputArray))