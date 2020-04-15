class Solution:
    # def checkIfMonoton(self, number: int) -> bool:
    #     n = [int(x) for x in str(number)]
    #     for i in range(len(n)-1):
    #         if n[i+1] < n[i]:
    #             return False
    #     return True



    # def monotoneIncreasingDigits(self, N: int) -> int:
    #     #n = [int(x) for x in str(N)]
    #     #print(n)
    #     #print(self.checkIfMonoton(n))

    #     while self.checkIfMonoton(N) == False:
    #         N -= 1
    #     return N
    

    def monotoneIncreasingDigits(self, N):
        digits = []
        A = map(int, str(N))
        for i in xrange(len(A)):
            for d in xrange(1, 10):
                if digits + [d] * (len(A)-i) > A:
                    digits.append(d-1)
                    break
            else:
                digits.append(9)

        return int("".join(map(str, digits)))
        
        





x = Solution()
n = 672766
print(x.monotoneIncreasingDigits(n))
