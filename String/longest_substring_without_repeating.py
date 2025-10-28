class Solution:
    def longest_substring_without_repeating_characters(self, s: str) -> int:
        string = []
        sub_string = ""
        max_len = 0
        for i in range(len(s)):
            if s[i] in sub_string:
                sub_string = ""
            else:
                sub_string += s[i]
                string.append(sub_string)
                max_len = max(max_len, len(sub_string))

        print(f"longest substring : {max(string,key = len)} , max length: {max_len}")
        return "Solved Successfully"


s = "abcabcbb"
print(Solution().longest_substring_without_repeating_characters(s))

s = "pwwkew"
print(Solution().longest_substring_without_repeating_characters(s))
