class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        target_char = 'B'
        countB = 0
        longest = ""

        current = ""  # build substring incrementally

        for ch in s:
            current += ch  # instead of s[:i+1]
            if ch == target_char:
                countB += 1

            if countB == k:
                # update longest substring
                if len(current) > len(longest):
                    longest = current

        updated = longest.replace('B', 'A')
        return len(updated)



# Example usage
s = "AABABBA"
k = 1
sol = Solution()
print(sol.characterReplacement(s, k))

s = "ABAB"
k = 2

print(sol.characterReplacement(s, k))
