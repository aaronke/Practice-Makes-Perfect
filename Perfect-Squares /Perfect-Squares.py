# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # Method 1 -- Recursion -- works but Time Exceed Limit
#         if n == 0:
#             return 0
#         num = 1
#         numList = []
#         while num**2 <= n:
#             numList.append(num**2)
#             num += 1
#         minSteps = 1+self.numSquares(n-numList[-1])
#         # for i in numList:
#         #     if (n-i >= 0) and ((1+self.numSquares(n-i)) < minSteps):
#         #         minSteps = 1+self.numSquares(n-i)

#         possibleNum = []
        
#         for i in numList:
#             if n-i**2 >= 0:
#                 possibleNum.append(1+self.numSquares(n-i**2))
#         return min(possibleNum)

#         # return minSteps

# import math
# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 0:
#             return 0
#         num = 1
#         numList = []
#         while num**2 <= n:
#             numList.append(num**2)
#             num += 1
#         possibleNum = []

        
#         minNum = 1+n-numList[-1]
#         for i in numList:
#             if n-i >= 0:
#                 temp =  1+self.numSquares(n-i)
#                 if temp < minNum:
#                     minNum = temp
        
#         return minNum     

class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            rs = []
            for i in range(1, int(len(dp)**0.5+1)):
                rs.append(dp[-i*i])
                # print dp[-i*i]
                # print dp
                # print -i*i

            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]  
        
s =  Solution()

print s.numSquares(35)