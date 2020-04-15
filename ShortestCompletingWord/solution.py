from typing import *

class Solution:
  
    def checkForShortestWord(self, results: list) -> str:
        length = float("inf")
        final = ""
        for word in results:
            if len(word) < length:
                length = len(word)
                final = word
        return final

    def createDictionary(self, letters: list):
        mydict = {}
        for letter in letters:
            mydict[letter] = letters.count(letter)
        return mydict


    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = []
        result = []
        for element in licensePlate:
            if element.isalpha():
                letters.append(element.lower())
        mydict = self.createDictionary(letters)
        #print(letters)
        #print(mydict)
        lettersCount = len(mydict)
        #print(lettersCount)
        check = 0
        for word in words:
            for key in mydict:
                if mydict[key] <= word.count(key):
                    check += 1
            #print("check {}".format(check))
            if check == lettersCount:
                result.append(word)
            check = 0
        
        answer = self.checkForShortestWord(result)
        return answer

       
            
        
        

        



licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]

x = Solution()
print(x.shortestCompletingWord(licensePlate, words))


letters = ["s", "p", "s", "t"]
word = "step"








