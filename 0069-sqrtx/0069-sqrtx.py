class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x>>1
        if x<2:
            return x
        while(left<=right):
            mid=(left+right)>>1
            if(mid*mid==x):
                return mid
            elif(mid**2<x):
                left=mid+1
            else:
                right=mid-1
        return left-1                