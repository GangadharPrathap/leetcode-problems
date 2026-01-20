class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        if n <= 26:
            s += chr(64+n)
        while n > 26:
            m = n % 26
            n = n // 26
            if not m:
                m = 26
                n -= 1
            if n > 26:
                s += chr(64+m)
                continue
            s +=  chr(64+m)
            s +=  chr(64+n)
        return s[::-1]   