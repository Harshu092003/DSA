class Solution:
    def common_prefix(self, s: list[str]) -> str:
        for i in range(len(s[0])):
            for word in s[1:]:
                if i >= len(word) or word[i] != s[0][i]:
                    return s[0][:i]

        return s[0]


s = ["flower", "flow", "flight"]
print(Solution().common_prefix(s))

print(Solution().common_prefix(["dog", "racecar", "car"]))
