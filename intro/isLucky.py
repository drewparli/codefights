"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;

For n = 239017, the output should be
isLucky(n) = false.
"""
def isLucky(n):
    digits = list(map(int, list(str(n))))
    size = len(digits)
    if size % 2 == 0:
        half = int(size / 2)
        left, right = digits[:half], digits[half:]
        return sum(left) == sum(right)
    else:
        return False


if __name__ == '__main__':

    # test 1
    n = 1230
    expected = True
    assert(isLucky(n) == expected)

    # # test 2
    n = 239017
    expected = False
    assert(isLucky(n) == expected)

    # # test 3
    n = 134008
    expected = True
    assert(isLucky(n) == expected)

    # # test 4
    n = 10
    expected = False
    assert(isLucky(n) == expected)

    # # test 5
    n = 11
    expected = True
    assert(isLucky(n) == expected)





