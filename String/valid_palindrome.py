class Solution:
    def valid_palindrome(self,text : str) -> bool :
        result = ""
        for ch in text :
            if ch.isalnum():
                result += ch.lower()
        
        return result == result[::-1]
    

text = "A man, a plan, a canal: Panama"
print(Solution().valid_palindrome(text))
print(''.join(s.lower() for s in text if s.isalnum()))
