# [Perfect Squares](https://leetcode.com/problems/perfect-squares/)

## Description
Given a positive integer n, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to n.

For example, given `n = 12`, return `3` because `12 = 4 + 4 + 4`; given `n = 13`, return `2` because `13 = 4 + 9`.
## Analysis
Method 1 -- Dynamic Programming. It costs a lot to do dynamic programming by using my own code. 

* Time complexity: `O(n)` `T(n) = K*T(n-1) + 1` K is the number of `int(math.sqrt(n))`.
* Space complexity: `O(n)`

Method 2 -- Consider the code in Leetcode [discussion](https://leetcode.com/discuss/56993/static-dp-c-12-ms-python-172-ms-ruby-384-ms)

To be undstood!!

Method 3 -- Dynamic Programming. The trick here is to use array to store the middle results. The Java implementation is [here](https://leetcode.com/discuss/57320/java-dp-solution-not-perfect-o-n-time-but-simple).

## Python Code
~~~Python
# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
         # Method 1 -- DP
#         if n == 0:
#             return 0
#         num = 1
#         numList = []
#         while num**2 <= n:
#             numList.append(num**2)
#             num += 1
#         possibleNum = []
        
#         for i in numList:
#             if n-i >= 0:
#                 possibleNum.append(1+self.numSquares(n-i))
        
#         return min(possibleNum)

# Method 1 -- Refined DP(Reduce the small computation cost and storage)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        num = 1
        numList = []
        while num**2 <= n:
            numList.append(num**2)
            num += 1
        possibleNum = []
        
        minNum = 1+self.numSquares(n-numList[-1])
        for i in numList:
            if n-i >= 0:
                temp = 1+self.numSquares(n-i)
                if temp < minNum:
                    minNum = temp
        
        return minNum  
# Method 2 -- Dynamic Programming!!
# class Solution(object):
#     _dp = [0]
#     def numSquares(self, n):
#         dp = self._dp
#         while len(dp) <= n:
#             rs = []
#             for i in range(1, int(len(dp)**0.5+1)):
#                 rs.append(dp[-i*i])
#             dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
#         return dp[n] 

        # Method 3 -- Dynamic Programming -- works but Time Exceed Limit-- Remeber to use array to store previous status
 #       if n == 0:
 #           return 0
 #       count = 1
 #       numList = [None]*n
 #       for i in range(n):
 #           if((i+1) == count*count):
 #               numList[i] = 1
 #               count += 1
 #           else:
 #               minVal = i+1
 #               for j in range(1, count):
 #                   if minVal > (numList[i-j*j]  + 1):
 #                       minVal = numList[i-j*j]  + 1
 #               numList[i] = minVal
 #       return numList[n-1]
~~~
## Notes
1. Remeber that when considering about dynamic programming, the index of array could be easily used to store the middle result.
