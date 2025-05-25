class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        n = nums[i]
        for j in range(i+1, len(nums)):
            if n != nums[j]:
                nums[i+1] = nums[j]
                i += 1
                n = nums[j]
        nums = nums[:i+1]
        return i+1
