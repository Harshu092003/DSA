class Solution:
    def wilcard_string_matching(self, wild: str, pattern: str):
        string = ""
        p_idx = 0

        for w in wild:
            if w == "?":
                string += pattern[p_idx]     
                p_idx += 1
            elif w == "*":
                string += pattern[p_idx:]    
                p_idx = len(pattern)
            else:  
                if p_idx >= len(pattern) or w != pattern[p_idx]:
                    return string ,True
                string += w
                p_idx += 1
        return string, True
print(Solution().wilcard_string_matching("ge*ks", "geeks"))
print(Solution().wilcard_string_matching("ge?ks*", "geeksforgeeks"))
print(Solution().wilcard_string_matching("ge?ks", "geeks"))
