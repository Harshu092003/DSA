class Solution:
    def max_subarray(self, nums: list[int], k: int) -> int:
        all_subarrays = []
        result = []

        # Generate all subarrays
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                all_subarrays.append(nums[i:j])

        # Check each subarray for divisibility
        for sub in all_subarrays:
            if sum(sub) % k == 0:
                result.append(sub)

        # Return the length of the longest valid subarray
        if result:
            longest = max(result, key=len)
            return len(longest), longest
        return 0


# Example
nums = [2, 7, 6, 1, 4, 5]
k = 3
print(Solution().max_subarray(nums, k))
