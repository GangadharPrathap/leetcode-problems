class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'()', '{}', '[]'}
        length = len(s)
        if length < 2:
            return not s
        i = 1
        while s:
            if s[i-1:i+1] in parentheses:
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                i += 1
            if i == length:
                break
        return not s
