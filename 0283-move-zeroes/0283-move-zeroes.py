from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0  # left part (non-zero zone)

        # fill left part with non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        # remaining positions → fill with 0
        for i in range(j, len(nums)):
            nums[i] = 0