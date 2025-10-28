from typing import List


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_so_far = min_so_far = result = nums[0]
        for i in range(1, len(nums)):
            candidates = (nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            result = max(result, max_so_far)
        return result


nums = [2, 3, -2, 4]
print(Solution().maxProduct(nums))
