class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = 0
        r = 1
        res = []

        # if nums is empty
        if not nums: 
            return res

        # if there is only one element in nums
        if len(nums) == 1:
            res.append(str(nums[0]))
            return res

        # two or more elements in nums
        while r < len(nums):

            if nums[r] == nums[r - 1] + 1:
                r += 1
            elif nums[r] != nums[r - 1] + 1 and l != r - 1:
                res.append(str(nums[l]) + "->" + str(nums[r - 1]))
                l = r
                r += 1
            elif nums[r] != nums[r - 1] + 1 and l == r - 1:
                res.append(str(nums[l]))
                l = r
                r += 1

            # check the last element of nums to not lose the last 
            # str list in nums for res
            if r == len(nums) and r == l + 1:
                res.append(str(nums[l]))
            elif r == len(nums) and r != l + 1:
                res.append(str(nums[l]) + "->" + str(nums[r - 1]))

        return res