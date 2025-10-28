class Solution:
    def remove_consecutive(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            if i == len(s) - 1 or s[i] != s[i + 1]:
                result += s[i]
        return result


s = "aabb"
print(Solution().remove_consecutive(s))

s = "aabaa"
print(Solution().remove_consecutive(s))
