from typing import *
from operator import itemgetter
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        a = sorted(costs, key= lambda x: x[0] -x[1])
        
        costs_A = 0
        costs_B = 0
        #print(a)
        
        for i in range(len(a)//2):
            costs_A += a[i][0]
        
        for i in range(len(a)//2, len(a)):
            costs_B += a[i][1]
        
        return costs_A + costs_B










costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
x = Solution()

print(x.twoCitySchedCost(costs))



# mydict = {}

# mydict[1] = "value"
# print(mydict)