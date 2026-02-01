class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3: return n

        n1=3
        n2=2
        cur=0
        
        for _ in range(3,n):
            cur=n1+n2
            n2=n1
            n1=cur
        return cur            