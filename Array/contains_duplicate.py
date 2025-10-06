from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True   # Found duplicate
            seen.add(num)
        return False          # No duplicates found
nums1 = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums1))

nums2 = [1, 2, 3, 4]
print(Solution().containsDuplicate(nums2))
