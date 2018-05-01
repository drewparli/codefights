"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""
def almostIncreasingSequence(sequence):
    result = True
    i, j = (0, 1)
    while j < len(sequence):
        if sequence[i] < sequence[j]:
            i = j
            j += 1
        else:
            left = sequence[0:i] + sequence[i+1:]
            right = sequence[0:j] + sequence[j+1:]
            result = isIncreasing(left) or isIncreasing(right)
            break
    return result

def isIncreasing(sequence):
    result = True
    i, j = (0, 1)
    while j < len(sequence):
        if not sequence[i] < sequence[j]:
            result = False
            break
        else:
            i = j
            j += 1
    return result