'''
    Given an array nums of n integers and an integer target, 
    find three integers in nums such that the sum is closest 
    to target. Return the sum of the three integers. You may 
    assume that each input would have exactly one solution.

    Example:
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. 
                 (-1 + 2 + 1 = 2).

    Constraints:
        - 3 <= nums.length <= 10^3
        - -10^3 <= nums[i] <= 10^3
        - -10^4 <= target <= 10^4
'''
#Difficulty: Medium
#131 / 131 test cases passed.
#Runtime: 1348 ms
#Memory Usage: 14.3 MB

#Runtime: 1348 ms, faster than 5.04% of Python3 online submissions for 3Sum Closest.
#Memory Usage: 14.3 MB, less than 42.23% of Python3 online submissions for 3Sum Closest.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float('inf')
        min_diff = float('inf')
        length = len(nums)

        for i in range(length - 2):
            left = i + 1
            right = length - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - current_sum)

                if diff < min_diff:
                    min_diff = diff
                    result = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target

        return result
