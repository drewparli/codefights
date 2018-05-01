"""
You have a string s that consists of English letters, punctuation
marks, whitespace characters, and brackets. It is guaranteed that
the parentheses in s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of
matching parentheses, starting from the innermost pair. The results
string should not contain any parentheses.

Example
=======
For string s = "a(bc)de", the output should be:
    reverseParentheses(s) = "acbde".

Input/Output
============
[execution time limit] 4 seconds (py3)

[input] string s

A string consisting of English letters, punctuation marks, whitespace characters and brackets. It is guaranteed that parentheses form a regular bracket sequence.

Constraints:
5 ≤ s.length ≤ 55.

[output] string
"""
def reverseParentheses(s):
    """Reverses the strings contained in each pair of matching
    parentheses, starting from the innermost pair. The resulting
    string does not contain any parentheses.

    See reverseInner().
    """
    return "".join(reverseInner(list(s)))

def reverseInner(s):
    """Helper function for reverseParentheses(), called recursively.

    Args:
        s(list) : The string as a list of characters

    Returns:
        result(list) : The resulting string without parentheses
    """
    result, inner = [], []
    level = 0
    for c in s:
        if (c is not "(") and (level == 0):
            # At the current level
            result.append(c)
        elif c is "(":
            # Leveling down
            level += 1
            inner.append(c)
        elif c is ")" and (level > 1):
            # Leveling up
            level -= 1
            inner.append(c)
        elif c is ")" and (level == 1):
            # Leveling up to the current level
            inner.append(c)
            # Throw away the outside parenthesis for inner
            inner = inner[1:-1]
            # Combine current result with reversed recursive call
            result += reverseInner(inner)[::-1]
            # Reset for remaining portion of string
            inner = []
            level = 0
        else:
            # At a sub-level, save characters for further processing
            inner.append(c)
    return result


if __name__ == '__main__':
    s = "a(bc)de"
    expected = "acbde"
    print(reverseParentheses(s))
    print(expected)

    s = "a(bcdefghijkl(mno)p)q"
    expected = "apmnolkjihgfedcbq"
    print(reverseParentheses(s))
    print(expected)

    s = "abc(cba)ab(bac)c"
    expected = "abcabcabcabc"
    print(reverseParentheses(s))
    print(expected)