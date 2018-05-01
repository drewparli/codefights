"""
Some people are standing in a row in a park. There are trees between
them which cannot be moved. Your task is to rearrange the people by
their heights in a non-descending order without moving the trees.

Example
=======
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be:

sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].


Input/Output
============

[execution time limit] 4 seconds (py3)

[input] array.integer a

If a[i] = -1, then the ith position is occupied by a tree.
Otherwise a[i] is the height of a person standing in the
ith position.

Guaranteed constraints:
5 ≤ a.length ≤ 15,
-1 ≤ a[i] ≤ 200.

[output] array.integer

Sorted array a with all the trees untouched.

"""
def sortByHeight(a):
    """Sort movable elements (people) by height (non-descending)
    inbetween the unmovable elements (trees)."""
    tree = -1
    heights = []
    pos = []

    # filter out the trees
    for (i,h) in enumerate(a):
        if h != tree:
            heights.append(h)
            pos.append(i)

    heights.sort()
    while heights:
        h = heights.pop(0)
        i = pos.pop(0)
        a[i] = h

    return a


if __name__ == '__main__':

    # test 1
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    expected = [-1, 150, 160, 170, -1, -1, 180, 190]
    assert(sortByHeight(a) == expected)