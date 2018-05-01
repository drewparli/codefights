"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase latin letters a-z.

Guaranteed constraints:
1 ≤ s1.length ≤ 15.

[input] string s2

A string consisting of lowercase latin letters a-z.

Guaranteed constraints:
1 ≤ s2.length ≤ 15.

[output] integer
"""
def commonCharacterCount(s1, s2):
    """Finds the number of common characters between two strings"""

    # don't destroy the inputs
    stringOne = list(s1)
    stringTwo = list(s2)

    # common char counter
    n = 0

    while stringOne:

        # consume a character from the first string
        char = stringOne.pop()

        if char in stringTwo:
            char_index = stringTwo.index(char)
            stringTwo.pop(char_index)
            n += 1

    return n