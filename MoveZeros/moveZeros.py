from typing import *


class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        print(nums)










test = Solution()
array = [0,1,0,3,12]
test.moveZeros(array)