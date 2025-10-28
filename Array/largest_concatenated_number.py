class Solution:
    def largest_concatenated(self, nums: list[int]) -> any:
        nums = list(map(str, nums))

        # Sort numbers based on repeating pattern logic
        nums.sort(
            key=lambda x: x * 10, reverse=True
        )  # used key to define custom behavior for sorting

        # Join sorted numbers
        result = "".join(nums)  # 9534330

        # Edge case: handle all zeros like [0, 0]
        return "0" if result[0] == "0" else result


nums = [3, 30, 34, 5, 9]
print(Solution().largest_concatenated(nums))
