class Solution :
    def longest_prefix_suffix(s : str) -> int :
        return max([i for i in range(1, len(s)) if s[:i] == s[-i:]] or [0])
print(Solution.longest_prefix_suffix("abab"))
print(Solution.longest_prefix_suffix("aaaa"))