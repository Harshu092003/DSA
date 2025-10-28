class Solution:
    def valid_anagram(self, s: str, t: str) -> bool:
        print(sorted(s))
        print(sorted(t))
        return sorted(s) == sorted(t)


print(Solution().valid_anagram("nagaram", "anagram"))
