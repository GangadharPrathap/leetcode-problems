class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            if(nums.count(i)!=1):
                return i