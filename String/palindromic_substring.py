class Solution :
    def palindromic_substring(self,s : str) -> int :
        result = []
        for i in range(len(s)) :
            result.append(s[i:i+3])
        
        for i in range(len(s)):
            substring = result[i]
            if substring == substring[::-1]:
                print(substring)
        return result
    
s = "babad"
print(Solution().palindromic_substring(s))