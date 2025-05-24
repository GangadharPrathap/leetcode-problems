class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        i = 0
        strs = sorted(strs, key=len)
        word = strs[0]
        for letter in word:
            if self.counter(strs[1:], letter, i):
                i += 1
            else: break
        return word[:i]

    def counter(self, strs, letter, i):
        for word in strs:
            if letter not in word[i]:
                return 0
        return 1
