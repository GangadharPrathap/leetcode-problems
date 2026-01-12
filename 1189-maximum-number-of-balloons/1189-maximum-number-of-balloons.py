class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        if not text:
            return 0
        
        import collections
        cnt = collections.Counter(text)
        cnt_ballon = collections.Counter('balloon')
        
        return min([cnt[c]//cnt_ballon[c] for c in cnt_ballon])