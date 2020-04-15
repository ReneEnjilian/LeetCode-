
from collections import Counter
from typing import List
from operator import itemgetter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number_dict = Counter(nums)
        result = max(number_dict.items(), key= itemgetter(1))[0]
        return result
        
            
       
       
        

        
        





x = Solution()
example = [6,5,5]
print(x.majorityElement(example))




