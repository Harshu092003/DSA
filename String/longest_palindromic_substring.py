class Solution:
    def longest_palindromic_substring(self, s: str) -> str:
        max_palindrome = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    if len(substring) > len(max_palindrome):
                       max_palindrome = substring 
        
        return max_palindrome
 
s = "babad"
print(Solution().longest_palindromic_substring(s))
