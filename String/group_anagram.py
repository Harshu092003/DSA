class Solution:
    def valid_anagram(self,strs : list[str] ) -> list[str] :
        result = {}
        for words in strs :
            key = ''.join(sorted(words))
            if key in result :
                result[key].append(words)
            else :
                result[key] = [words]

        return result.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().valid_anagram(strs))