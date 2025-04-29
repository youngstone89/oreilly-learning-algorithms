
# quick select
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[len(nums) - k]


def find_kth_largest_2(nums: List[int], k: int) -> int:
    # find the index of number that corresponds to kth largest
    k = len(nums) - k

    def quick_select(l, r):
        # set the right most value as pivot, set the pivot pointer to the left most value
        pivot, p = nums[r], l
        # loop through each value from left to right (excluding right most value)
        for i in range(l, r):
            # check if ith element is less than equal to the pivot for swap
            if nums[i] <= pivot:
                # swap i and p and increase pivot pointer
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        # after entire traverse, swap numbers at pivot pointer and the right most value
        # for partitioning ( meaning left hand side is less than, right hand side is greather than)
        nums[p], nums[r] = nums[r], nums[p]
        # decide which side to look at for search
        # if the target index "k" is smaller than the pivot pointer "p", we have to look at left hand side
        if p > k:
            return quick_select(l, p - 1)
        # if the target index "k" is greater than the pivot pointer "p", we have to look at right hand side
        elif p < k:
            return quick_select(p + 1, r)
        # other wise, return the number a "p" index as that's the number we are targeting.
        else:
            return nums[p]

    return quick_select(0, len(nums)-1)


nums = [3, 2, 1, 5, 6, 4]

print(find_kth_largest(nums, 2))
print(find_kth_largest_2(nums, 2))
