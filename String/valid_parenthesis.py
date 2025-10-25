class Solution:
    def valid_parenthesis(self, s: str) -> bool:
        stack = []
        pairs = {'(' : ')', '[' : ']', '{' : '}'}

        for ch in s:
            if ch in pairs:  # opening bracket
                stack.append(ch)
            elif stack and ch == pairs[stack[-1]] : # match top’s closing pair
                stack.pop()
            else:
                return False

        return not stack




print(Solution().valid_parenthesis("()"))        # True
print(Solution().valid_parenthesis("()[]{}"))    # True
print(Solution().valid_parenthesis("(]"))        # False
print(Solution().valid_parenthesis("([])"))      # True
print(Solution().valid_parenthesis("([)]"))      # False
