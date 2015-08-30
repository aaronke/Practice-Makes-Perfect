# [Missing Number](https://leetcode.com/problems/missing-number/)

## Description
Given an array containing n distinct numbers taken from `0, 1, 2, ..., n,` find the one that is missing from the array.

For example,
Given nums = `[0, 1, 3]` return 2.

Note: Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

## Analysis
Method 1 -- Sum: The first idea is to sum the numbers of two lists respectively and if the difference is 0, then they are the same, otherwise, it will be the missing number. Someone claims the weakness for this method is the risk of overflow.  calculating sum has potential to cause overflow.

* Time Complexsity: `O(n)`
* Space Complexity: `O(1)`

Method 2 -- Bit operation: Because `A xor A = 0`, and also XOR operator is commutative(交换性). So if connecting two number lists and do XOR operation for all the elements, the result would be 0 if two number lists are the same (without missing number)
* Time Complexsity: `O(n)`
* Space Complexity: `O(n)`


## Python Code
~~~python
import operator # Only for method 2
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1 -- sum
        # n = len(nums)
        # sumNums = 0
        # for i in nums:
        #     sumNums = sumNums + i
        
        # return ((n +1) * n)/2 - sumNums
        
        # Method 2 -- bit manipulation
        return reduce(operator.xor,range(len(nums)+1) + nums)
~~~        

## Notes
1. Important build-in functions in python -`map, filter, reduce, lambda operator`.
 
`reduce` will apply input function and return a final value. `filter` will return the list with the elements what make input function return true. `map` will apply input function to all elements and return new list.  
More information --Tutorial [Link](http://www.python-course.eu/lambda.php)   

