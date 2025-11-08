class Solution:
    def smallest_substring_contain_all_characters(self, s: str, p: str) -> str:
        result = []
        length = len(p)

        for i in range(len(s)):
            result.append(s[i:i + length])
            result.append(s[i:i + length + 1])
            result.append(s[i:i + length + 2])
            result.append(s[i:i + length + 3])

        cleaning = set()
        for item in result:
            cleaning.add(item)

        smallest = ""

        for sub in cleaning :
            if all(c in sub for c in p):
                smallest = sub
                break
            
        return smallest

    
s = "timetopractice"
p = "toc"

print(Solution().smallest_substring_contain_all_characters(s,p))