from typing import List
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        
        lower_count = 0
        firstLetter = word[0]
        for i in range(1, len(word)):
            if word[i].islower():
                lower_count += 1

        if lower_count == len(word)-1 or (lower_count == 0 and not firstLetter.islower()) :
            return True
        else:
            return False







test = Solution()
word = "google"
print(test.detectCapitalUse(word))