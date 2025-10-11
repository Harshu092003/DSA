class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        # Left pass: result[i] contains product of all elements to the left
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Right pass: multiply result[i] by product of all elements to the right
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result


nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))
        



