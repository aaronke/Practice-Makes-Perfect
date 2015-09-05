class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Method 1 - Naive
        # if num < 10:
        #     return num
        # digits = []
        # while num:
        #      digits.append(num%10)
        #      num =  num/10
    
        # return self.addDigits(sum(digits))
        
        # Method 2 - Mode 
        if num < 10:
            return num
        rs =  num % 9
        return rs if rs != 0 else 9


s = Solution()
print s.addDigits(38)