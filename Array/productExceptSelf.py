class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        # Prefix: product of all elements to the left
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Suffix: product of all elements to the right
        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i + 1]
            result[i] *= suffix

        return result


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
