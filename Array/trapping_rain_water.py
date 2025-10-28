from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0  # Return 0 instead of None

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water


# Test examples
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))  # Output: 6

height = [4, 2, 0, 3, 2, 5]
print(Solution().trap(height))  # Output: 9
