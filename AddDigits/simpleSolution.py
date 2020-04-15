from typing import *

class Solution:

    def __init__(self):
        self.result = float("inf")

    def addDigits(self, num: int) -> int:

        while(num >= 10):
            numberList = [int(x) for x in str(num)]
            num = sum(numberList)
        return num 

        

        



x = Solution()
test = 49
print(x.addDigits(test))

