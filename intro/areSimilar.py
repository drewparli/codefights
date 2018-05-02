"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Array of integers.

Guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[input] array.integer b

Array of integers of the same length as a.

Guaranteed constraints:
b.length = a.length,
1 ≤ b[i] ≤ 1000.

[output] boolean

true if a and b are similar, false otherwise.
"""
def areSimilar(a, b):
    """Checks if two arrays of equal length are similar."""

    # Find values `a` and `b` that don't match up
    A = []
    B = []
    for i,aVal in enumerate(a):
        bVal = b[i]
        # check at each vertical position
        if aVal != bVal:
            # save values, but swap B's order
            A.append(aVal)
            B.insert(0, bVal)

    # The length of A (and thus B) helps us know if it is
    # possible for the arrays to be similar.
    n = len(A)

    # a == b
    if n == 0:
        return True

    # only 2 values didn't match, check the saved swap
    if n == 2 and A == B:
        return True

    return False


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [2, 1, 3]
    result = areSimilar(a, b)
    print(result)

    a = [2, 3, 1]
    b = [1, 3, 2]
    result = areSimilar(a, b)
    print(result)