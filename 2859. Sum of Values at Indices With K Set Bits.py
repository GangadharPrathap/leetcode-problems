class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total_sum = 0
        for i in range(len(nums)):
            # Count the number of set bits in the binary representation of index i
            set_bits_count = 0
            num = i
            while num > 0:
                num &= (num - 1) # This trick removes the least significant set bit
                set_bits_count += 1
            
            # If the count of set bits equals k, add the number to the total_sum
            if set_bits_count == k:
                total_sum += nums[i]
                
        return total_sum
