class Solution:
    def duplicate_characters(self, s: str) -> dict:
        result = {}  # dictionary to store {char: count}

        for word in s:
            if word in result:
                result[word] += 1  # increment count if seen before
            else:
                result[word] = 1   # first occurrence, set count = 1

        return {ch:count for ch,count in result.items() if count>1 }

        


s = "geeksforgeeks"
print(Solution().duplicate_characters(s))

# Input: s = "geeksforgeeks"
# Output: ['e', 4], ['g', 2], ['k', 2], ['s', 2]
# Explanation: Characters e, g, k, and s appear more than once. Their counts are shown in order of first occurrence.

# Input: s = "programming"
# Output: ['r', 2], ['g', 2], ['m', 2]
# Explanation: Only r, g, and m are duplicates. Output lists them with their counts.