from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current and global maximum
        max_current = max_global = nums[0]
        
        # Loop through array starting from the 2nd element
        for i in range(1, len(nums)):
            # Update current max (either start new subarray or add to existing one)
            max_current = max(nums[i], max_current + nums[i])
            
            # Update global max if needed
            max_global = max(max_global, max_current)
        
        return max_global


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))
