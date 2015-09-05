# [Add Digits](https://leetcode.com/problems/add-digits/)
 
## Description
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

**Follow up:** Could you do it without any loop/recursion in O(1) runtime?

## Analysis
**Method 1 -- Naive** So just use while loop and recursion for geting the digts and get the number.

**Method 1 -- Mode**  Firstly, think about what the possible results are. It's 0~9. And then How can we get 0~9？ Firstly, I think about get a array with the length of 10. However, it's still hard to get O(1) complexity. However, the final answer is simple and tuitive -- mode number with 9. Think abouting in another way, if moding with 9, it means it will get its digits and sum them, and mode with 9 again.

## Python Code
~~~
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
~~~

## Notes
1. If `dn` is defined as the `n-th` digit for number, then for our definition, it is to get the sum of `dn + .... + d2 + d1` and do the same thing. If our definition changes as geting the sum of `dn*2 + .... + d2*2 + d1`, then the algorithm could be change from mode 9 to mode 8.

