from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)

        for pos in groups.values():
            m = len(pos)
            if m <= 1:
                continue

            prefix = [0] * m
            prefix[0] = pos[0]
            for i in range(1, m):
                prefix[i] = prefix[i - 1] + pos[i]

            # For each position pos[k] in this group:
            # left sum = sum(pos[k] - pos[j]) for j < k
            # right sum = sum(pos[j] - pos[k]) for j > k
            for k in range(m):
                left_count = k
                right_count = m - k - 1

                # sum of positions on the left: prefix[k-1]
                left_sum_positions = prefix[k - 1] if k > 0 else 0
                # left contribution: left_count * pos[k] - sum(left positions)
                left = left_count * pos[k] - left_sum_positions

                # sum of positions on the right: prefix[m-1] - prefix[k]
                total_positions = prefix[m - 1]
                right_sum_positions = total_positions - prefix[k]
                # right contribution: sum(right positions) - right_count * pos[k]
                right = right_sum_positions - right_count * pos[k]

                ans[pos[k]] = left + right

        return ans