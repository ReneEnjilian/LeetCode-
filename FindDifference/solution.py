from typing import List

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s_list = list(s)
        t_list = list(t)
        
        for i in range(len(s_list)):
            for j in range(len(t_list)):
                if s_list[i] == t_list[j]:
                    t_list.remove(t_list[j])
                    break
        
        return t_list[0]






x = Solution()
s = "abcd"
t = "abcde"
print(x.findTheDifference(s,t))
