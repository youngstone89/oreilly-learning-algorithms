import random
from typing import List


def partition(A, lo, hi, idx):
    # return low value if hi and lo are equal, meaning no more dividing
    if lo == hi:
        return lo

    A[idx], A[lo] = A[lo], A[idx]
    i = lo  # increase index from the lowest point
    j = hi + 1  # decrease index from the highest point

    while True:
        while True:
            i += 1  # increase index by 1
            if i == hi:
                break  # break out of first inner loop when index has reached highest point

            # stop when value of index i is greater than low index value
            if A[lo] < A[i]:
                break

        while True:
            j -= 1  # decrease index by 1
            if j == lo:
                break  # stop when the index has reached the lowest point
            if A[j] < A[lo]:
                break  # stop when the value of index j is less than the low index value

        if i >= j:
            break  # break out of outer loop when i is greater than equal to j
        A[i], A[j] = A[j], A[i]  # swap i and j values

    A[lo], A[j] = A[j], A[lo]  # swap low and j index value
    return j


def linear_median(A: List[int]):
    lo = 0
    hi = len(A) - 1
    mid = hi // 2

    while lo < hi:
        idx = random.randint(lo, hi)
        j = partition(A, lo, hi, idx)

        if j == mid:
            return A[j]
        if j < mid:
            lo = j + 1
        else:
            hi = j - 1
    return A[lo]


# print(linear_median([1, 2, 3, 4, 5]))


print(linear_median([9, 2, 6, 4, 11, 15]))
