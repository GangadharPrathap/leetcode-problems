class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)-1
        while val in nums:
            if nums[length] == val:
                nums.pop(length)
            length-=1    
        return len(nums)
