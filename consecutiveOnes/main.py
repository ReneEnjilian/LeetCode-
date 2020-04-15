class Solution:

    def __init__(self):
        self.count_list = []
        self.count = 0
        self.temp = 0

    def findMaxConsecutiveOnes(self, nums: list) -> int:
        for i in range(len(nums)):
            if nums[i] == 1:
                self.count = self.count + 1

            if nums[i] == 0 or i == len(nums)-1:
                if self.count > self.temp:
                    self.temp = self.count
                self.count = 0

        return self.temp 
            
            
      
            
            






s = Solution()
first = [1,1,0,1,1,1]
print(s.findMaxConsecutiveOnes(first))



t = Solution()
second = [1,1,1,1]
print(t.findMaxConsecutiveOnes(second))


r = Solution()
third = [0 for i in range(5)]
print(r.findMaxConsecutiveOnes(third))

g = Solution()
fourth = [1,1,1,0,1,1]
print(g.findMaxConsecutiveOnes(fourth))

