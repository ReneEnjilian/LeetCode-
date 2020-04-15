import typing
from typing import *

class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        asc = sorted(A)
        desc = sorted(A, reverse=True)

        if A == asc or A == desc:
            return True
        else:
            return False





h = Solution()
array = [1,3,2]
print(h.isMonotonic(array))




