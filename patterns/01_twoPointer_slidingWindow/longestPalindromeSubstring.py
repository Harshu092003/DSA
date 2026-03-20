class Solution(object):
    def longestSubstring(self, s):
        """
        Sliding Window / Two Pointer Pattern

        left  → start of window
        right → end of window

        We move right step by step (expand),
        and move left only when needed (shrink).

        Goal:
        Maintain a window with NO duplicate characters.
        """

        char_set = set()
        left = 0
        right = 0

        max_length = 0
        start = 0

        while right < len(s):

            # If duplicate → shrink window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add current character (expand window)
            char_set.add(s[right])

            # Update best answer
            if right - left + 1 > max_length:
                max_length = right - left + 1
                start = left

            # Move right pointer
            right += 1

        return s[start:start + max_length], max_length

sol = Solution()
print(sol.longestSubstring("abcabcbb"))  # ('abc', 3)
print(sol.longestSubstring("pwwkew"))    # ('wke', 3)
print(sol.longestSubstring("bbbbb"))     # ('b', 1)