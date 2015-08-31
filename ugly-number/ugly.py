import math
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = 1
        # start = 1
        # temp = 0
        # if n == 1:
        #     return start
        # while (count < n):
        #     start += 1
        #     # if self.checkUgly(start):
        #     temp = start
        #     while temp%2 == 0:
        #         temp =  temp/2
        #     while temp%3 == 0:
        #         temp =  temp/3
        #     while temp%5 == 0:
        #         temp =  temp/5
        #     if temp == 1:
        #         count += 1
        # return start

        if n == 1:
            return 1
            
        count = 2
        v = 2
        x2 = 1
        x3 = 0
        x5 = 0
        
        while( n > count):
            minSum = int(math.floor(math.log(v,5)))
            maxSum = int(math.ceil(math.log(v,2)))
            nextValue = 5**maxSum
            for tempSum in range(minSum, maxSum+1):
                for tempX2 in range(tempSum+1):
                    for tempX3 in range(tempSum-tempX2+1):
                        for tempX5 in range(tempSum-tempX2-tempX3+1):
                            newValue = (2**tempX2) * (3**tempX3) * (5**tempX5)
                            if (v < newValue and nextValue > newValue):
                                nextValue = newValue
            v = nextValue
            count += 1
        return v

s = Solution()
print s.nthUglyNumber(279)