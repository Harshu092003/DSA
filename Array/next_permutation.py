from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # S Find first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        #  If found, find the next bigger element on right side
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]

        #  Reverse the remaining right half
        nums[i + 1 :] = reversed(nums[i + 1 :])


nums = [1, 2, 3]
Solution().nextPermutation(nums)
print(nums)
