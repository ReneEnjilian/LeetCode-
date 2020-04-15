import typing
from typing import *

class Solution:
    def __init__(self):
        self.result = []


    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and nums1[i] not in self.result:
                    self.result.append(nums1[i])
                    #print(self.result)
        return self.result
                    







first = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(first.intersection(nums1, nums2))