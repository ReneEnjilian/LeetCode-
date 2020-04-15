import typing
from typing import *


class Solution:
    
    def __init__(self):
        self.result = []
        self.finished = False
    

    def arrayNesting(self, nums : List[int]) -> int:
        item = nums[0]
        self.result.append(item)
        while(self.finished == False):
            if nums[item] not in self.result:
                item = nums[item]
                #print(item)
                self.result.append(item)
                #print(self.result)
            else:
                self.finished = True
                #print(self.result)
                
                print("ende")
                return self.result
            
            
    
            
            




s = Solution()

B = list(range(1,6))
B.append(0)
#print(B)
print(s.arrayNesting(B))



#test 2
t = Solution()

A = [5,4,0,3,1,6,2]
print(t.arrayNesting(A))

r = Solution()
x = [0,2,1]
print(r.arrayNesting(x))

