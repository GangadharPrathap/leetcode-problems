class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_number = -2**31
        max_number = 2**31 - 1
        result = abs(dividend) // abs(divisor)
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return min(result, max_number)
        else:
             return max(-result, min_number)